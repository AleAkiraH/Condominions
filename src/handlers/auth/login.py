import json
import boto3
import bcrypt
import jwt
from datetime import datetime, timedelta

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('condominions-users')
JWT_SECRET = 'seu_jwt_secret'  # Mova para variáveis de ambiente

def handler(event, context):
    try:
        body = json.loads(event['body'])
        
        if not all(k in body for k in ['email', 'password']):
            return {
                'statusCode': 400,
                'body': json.dumps({'message': 'Email e senha são obrigatórios'})
            }
            
        # Buscar usuário
        response = table.get_item(
            Key={
                'pk': f"USER#{body['email']}",
                'sk': 'PROFILE'
            }
        )
        
        if 'Item' not in response:
            return {
                'statusCode': 401,
                'body': json.dumps({'message': 'Credenciais inválidas'})
            }
            
        user = response['Item']
        
        # Verificar senha
        if not bcrypt.checkpw(body['password'].encode('utf-8'), 
                            user['password'].encode('utf-8')):
            return {
                'statusCode': 401,
                'body': json.dumps({'message': 'Credenciais inválidas'})
            }
            
        # Gerar token JWT
        token = jwt.encode(
            {
                'user_id': user['email'],
                'exp': datetime.utcnow() + timedelta(days=1)
            },
            JWT_SECRET,
            algorithm='HS256'
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'token': token,
                'user': {
                    'email': user['email'],
                    'name': user['name'],
                    'apartment': user['apartment']
                }
            })
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': str(e)})
        }
