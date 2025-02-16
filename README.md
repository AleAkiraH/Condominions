# Condominions - Sistema de Gestão de Condomínio

Sistema serverless para gestão de condomínios utilizando AWS Lambda, API Gateway e DynamoDB.

## 🚀 Tecnologias

- Python 3.9
- AWS Lambda
- Amazon API Gateway
- Amazon DynamoDB
- AWS SES (Simple Email Service)
- Serverless Framework
- JWT para autenticação

## 📋 Pré-requisitos

- Node.js e NPM
- Python 3.9
- AWS CLI configurado
- Serverless Framework
- Docker (para build das dependências)

## 🔧 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/Condominions.git
cd Condominions
```

2. Instale as dependências:
```bash
npm install
pip install -r requirements.txt
```

3. Configure as variáveis de ambiente:
```bash
cp .env.example .env
# Edite o arquivo .env com suas configurações
```

4. Deploy da aplicação:
```bash
serverless deploy
```

## 🛠️ Endpoints

### Autenticação

- `POST /auth/register` - Registro de novo usuário
- `POST /auth/login` - Login de usuário
- `POST /auth/forgot-password` - Solicitar recuperação de senha
- `POST /auth/reset-password` - Resetar senha com token
- `PUT /auth/profile` - Atualizar perfil do usuário
- `POST /auth/change-password` - Alterar senha
- `POST /auth/logout` - Logout do usuário

## 📦 Estrutura do Projeto

```
Condominions/
├── src/
│   ├── auth/
│   │   ├── register.py
│   │   ├── login.py
│   │   ├── forgot_password.py
│   │   ├── reset_password.py
│   │   ├── update_profile.py
│   │   └── logout.py
│   └── shared/
│       ├── models/
│       │   └── user.py
│       ├── auth.py
│       ├── email.py
│       └── response.py
├── tests/
├── serverless.yml
├── requirements.txt
├── package.json
└── README.md
```

## 🔐 Segurança

- Senhas criptografadas com bcrypt
- Autenticação via JWT
- CORS habilitado
- Validação de inputs
- Rate limiting na API

## 📝 DynamoDB Schema

### Users Table
- PK: USER#{email}
- SK: PROFILE
- Atributos:
  - email
  - name
  - password (hashed)
  - phone
  - apartment_number
  - created_at
  - updated_at
  - reset_token (opcional)

## 🧪 Testes

Para executar os testes:
```bash
pip install pytest
pytest
```

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## ✒️ Autores

* **Seu Nome** - *Trabalho Inicial* - [SeuUsuario](https://github.com/SeuUsuario)

## 🎁 Expressões de Gratidão

* Compartilhe este projeto 📢
* Convide alguém da equipe para uma cerveja 🍺
* Obrigado publicamente 🤓

---
⌨️ com ❤️ por [Seu Nome](https://github.com/SeuUsuario) 😊
