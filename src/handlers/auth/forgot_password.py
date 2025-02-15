import json
import boto3
import uuid
from datetime import datetime, timedelta

dynamodb = boto3.resource('dynamodb')
ses = boto3.client('ses')
table = dynamodb.Table('condominions-users')

def handler(event, context):
    try:
        body = json.loads(event['body'])
        email = body.get('email')
        
        if not email:
            return {
                'statusCode': 400,
                'body': json.dumps({'message': 'Email é obrigatório'})
            }
            
        # Gerar token de reset
        reset_token = str(uuid.uuid4())
        expiration = datetime.now() + timedelta(hours=1)
        
        # Salvar token no DynamoDB
        table.update_item(
            Key={
                'pk': f"USER#{email}",
                'sk': 'PROFILE'
            },
            UpdateExpression='SET reset_token = :token, reset_expiration = :exp',
            ExpressionAttributeValues={
                ':token': reset_token,
                ':exp': expiration.isoformat()
            }
        )
        
        # Enviar email usando SES
        reset_link = f"https://seudominio.com/reset-password?token={reset_token}"
        ses.send_email(
            Source='seu-email-verificado@dominio.com',
            Destination={'ToAddresses': [email]},
            Message={
                'Subject': {'Data': 'Recuperação de Senha'},
                'Body': {
                    'Text': {'Data': f'Use este link para resetar sua senha: {reset_link}'}
                }
            }
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Email de recuperação enviado'})
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': str(e)})
        }
