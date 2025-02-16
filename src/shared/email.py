import boto3

def send_reset_password_email(email, reset_token):
    ses = boto3.client('ses')
    
    subject = 'Recuperação de Senha - Condominions'
    body = f'Use este link para resetar sua senha: {reset_token}'
    
    ses.send_email(
        Source='seu-email-verificado@dominio.com',
        Destination={'ToAddresses': [email]},
        Message={
            'Subject': {'Data': subject},
            'Body': {'Text': {'Data': body}}
        }
    )

def send_delivery_notification(email, pickup_code, description):
    ses = boto3.client('ses')
    
    subject = 'Nova Entrega - Condominions'
    body = f"""
    Olá!
    
    Uma nova entrega foi registrada para você:
    
    Descrição: {description}
    Código de Retirada: {pickup_code}
    
    Por favor, utilize este código ao retirar sua entrega na portaria.
    
    Atenciosamente,
    Equipe Condominions
    """
    
    ses.send_email(
        Source='seu-email-verificado@dominio.com',
        Destination={'ToAddresses': [email]},
        Message={
            'Subject': {'Data': subject},
            'Body': {'Text': {'Data': body}}
        }
    )
