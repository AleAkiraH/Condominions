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
