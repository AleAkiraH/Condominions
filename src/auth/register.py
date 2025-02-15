import json
import logging
import boto3
import bcrypt
from src.shared.response import build_response

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('condominions-users')

def handler(event, context):
    logger.info(f"Received event: {json.dumps(event)}")
    
    try:
        if not event.get('body'):
            return build_response(400, {"message": "Invalid request"})
            
        body = json.loads(event['body'])
        
        # Validate required fields
        required_fields = ['email', 'password', 'name', 'phone']
        for field in required_fields:
            if field not in body:
                return build_response(400, {"message": f"Missing required field: {field}"})

        email = body['email']
        password = body['password']
        name = body['name']
        phone = body['phone']

        # Check if user already exists
        existing_user = table.get_item(
            Key={
                'pk': f'USER#{email}',
                'sk': 'PROFILE'
            }
        ).get('Item')
        
        if existing_user:
            return build_response(400, {"message": "User already exists"})

        # Hash the password
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        
        # Save user to DynamoDB
        table.put_item(
            Item={
                'pk': f'USER#{email}',
                'sk': 'PROFILE',
                'name': name,
                'phone': phone,
                'password': hashed.decode('utf-8')
            }
        )
        
        return build_response(201, {"message": "User registered successfully"})
        
    except json.JSONDecodeError as e:
        logger.error(f"JSON decode error: {e}")
        return build_response(400, {"message": "Invalid JSON"})
        
    except Exception as e:
        logger.error(f"Error: {e}")
        return build_response(500, {"message": "Internal server error"})
