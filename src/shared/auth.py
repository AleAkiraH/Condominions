import jwt
from datetime import datetime, timedelta

def generate_token(user_id):
    exp = datetime.utcnow() + timedelta(days=1)
    return jwt.encode(
        {'user_id': user_id, 'exp': exp},
        'seu-secret-aqui',
        algorithm='HS256'
    )

def verify_token(token):
    try:
        return jwt.decode(
            token,
            'seu-secret-aqui',
            algorithms=['HS256']
        )
    except:
        return None
