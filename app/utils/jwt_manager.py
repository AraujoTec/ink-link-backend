from app.authenticate.models import User
from app import settings
from datetime import datetime, timedelta
import jwt

def generate_jwt_token(usuarios: User, expiration_time_in_hours: int = 1):
    secret_key = settings.SECRET_KEY

    expiration_time = datetime.utcnow() + timedelta(hours=expiration_time_in_hours)

    payload = {
        "usuario_id": str(usuarios.id),
        "empresa_id": str(usuarios.empresa_id),
        "exp": expiration_time,
        "name": f"{usuarios.first_name} {usuarios.last_name}"
    }

    token = jwt.encode(payload, secret_key, algorithm="HS256")
    return token



def decode_jwt_token(token: str):
    secret_key = settings.SECRET_KEY
    if 'Bearer' in token:
        token = token.split(' ')[1]
    return jwt.decode(token, secret_key, algorithms=["HS256"])

def authenticate(request):
    authorization = request.headers.get("Authorization")
    return decode_jwt_token(authorization)