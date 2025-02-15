import json
import boto3
import bcrypt
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('condominions-users')

def handler(event, context):
    try:
        body = json.loads(event['body'])
        
        # Validação dos campos obrigatórios
        required_fields = ['name', 'email', 'password', 'apartment']
        if not all(field in body for field in required_fields):
            return {
                'statusCode': 400,
                'body': json.dumps({'message': 'Campos obrigatórios faltando'})
            }
            
        # Hash da senha
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(body['password'].encode('utf-8'), salt)
        
        # Criar usuário no DynamoDB
        user_item = {
            'pk': f"USER#{body['email']}",
            'sk': 'PROFILE',
            'email': body['email'],
            'name': body['name'],
            'apartment': body['apartment'],
            'password': hashed.decode('utf-8'),
            'created_at': datetime.now().isoformat(),
            'type': 'USER'
        }
        
        table.put_item(
            Item=user_item,
            ConditionExpression='attribute_not_exists(pk)'
        )
        
        return {
            'statusCode': 201,
            'body': json.dumps({
                'message': 'Usuário criado com sucesso',
                'user': {
                    'email': body['email'],
                    'name': body['name'],
                    'apartment': body['apartment']
                }
            })
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': str(e)})
        }
