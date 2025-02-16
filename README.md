# Condominions API

API para gestão de condomínios com foco em controle de entregas.

## 🚀 Setup

```bash
npm install
pip install -r requirements.txt
serverless deploy
```

## 📚 Endpoints

### 🔑 Autenticação

#### POST /auth/register
```json
// Request
{
    "email": "user@example.com",
    "password": "Senha@123",
    "name": "Nome Completo",
    "phone": "+5511999999999",
    "apartment_number": "42A"
}

// Response 200
{
    "message": "User created successfully",
    "user": {
        "email": "user@example.com",
        "name": "Nome Completo",
        "phone": "+5511999999",
        "apartment_number": "42A"
    }
}
```

#### POST /auth/login
```json
// Request
{
    "email": "user@example.com",
    "password": "Senha@123"
}

// Response 200
{
    "message": "Login successful",
    "token": "jwt.token.here"
}
```

### 📦 Entregas

#### POST /deliveries
```json
// Request
{
    "resident_name": "Nome Morador",
    "apartment_number": "42A",
    "description": "Pacote Amazon - 2 volumes"
}

// Response 201
{
    "message": "Delivery registered successfully",
    "delivery": {
        "delivery_id": "uuid-here",
        "pickup_code": "ABC123",
        "status": "PENDING"
    }
}
```

#### POST /deliveries/{id}/confirm
```json
// Request
{
    "pickup_code": "ABC123"
}

// Response 200
{
    "message": "Delivery confirmed successfully"
}
```

#### GET /deliveries
```json
// Response 200
{
    "deliveries": [
        {
            "delivery_id": "uuid-here",
            "resident_name": "Nome Morador",
            "apartment_number": "42A",
            "description": "Pacote Amazon - 2 volumes",
            "status": "PENDING",
            "created_at": "2024-02-15T10:00:00Z"
        }
    ]
}
```

## 🔐 Autorização

Para rotas protegidas, adicione o header:
```
Authorization: Bearer {token}
```

## 📝 Schema DynamoDB

### Users Table
- PK: USER#{email}
- SK: PROFILE

### Deliveries Table
- PK: DELIVERY#{apartment_number}
- SK: DELIVERY#{timestamp}
- GSI1: delivery_id
- GSI2: status, created_at
