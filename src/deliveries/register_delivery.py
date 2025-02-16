import json
import logging
import boto3
from datetime import datetime
from src.shared.models.delivery import Delivery
from src.shared.response import build_response
from src.shared.email import send_delivery_notification

logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('condominions-users')

def handler(event, context):
    try:
        if not event.get('body'):
            return build_response(400, {"message": "Invalid request"})
            
        body = json.loads(event['body'])
        
        # Validar campos obrigatórios
        required_fields = ['resident_name', 'apartment_number', 'description']
        for field in required_fields:
            if field not in body:
                return build_response(400, {"message": f"Missing required field: {field}"})

        delivery = Delivery()
        delivery.resident_name = body['resident_name']
        delivery.apartment_number = body['apartment_number']
        delivery.description = body['description']
        delivery.created_by = event['requestContext']['authorizer']['principalId']
        
        # Criar registros na DynamoDB
        delivery_item = {
            'pk': f"DELIVERY#{delivery.apartment_number}",
            'sk': f"DELIVERY#{delivery.created_at}",
            'delivery_id': delivery.delivery_id,
            'resident_name': delivery.resident_name,
            'apartment_number': delivery.apartment_number,
            'description': delivery.description,
            'pickup_code': delivery.pickup_code,
            'status': delivery.status,
            'created_at': delivery.created_at,
            'created_by': delivery.created_by
        }
        
        table.put_item(Item=delivery_item)
        
        # Buscar email do morador
        resident = table.get_item(
            Key={
                'pk': f"USER#{delivery.apartment_number}",
                'sk': 'PROFILE'
            }
        ).get('Item')
        
        if resident and resident.get('email'):
            # Enviar notificação por email
            send_delivery_notification(
                resident['email'], 
                delivery.pickup_code,
                delivery.description
            )
        
        return build_response(201, {
            "message": "Delivery registered successfully",
            "delivery": delivery_item
        })
        
    except Exception as e:
        logger.error(f"Error: {e}")
        return build_response(500, {"message": "Internal server error"})
