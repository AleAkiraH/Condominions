import json
import logging
import boto3
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
        
        email = body['email']

        # Get user from DynamoDB
        user = table.get_item(
            Key={
                'pk': f'USER#{email}',
                'sk': 'PROFILE'
            }
        ).get('Item')
        
        if not user:
            return build_response(400, {"message": "User not found"})

        # Logic to handle password reset (e.g., send email with reset link)
        
        return build_response(200, {"message": "Password reset email sent"})
        
    except json.JSONDecodeError as e:
        logger.error(f"JSON decode error: {e}")
        return build_response(400, {"message": "Invalid JSON"})
        
    except Exception as e:
        logger.error(f"Error: {e}")
        return build_response(500, {"message": "Internal server error"})
