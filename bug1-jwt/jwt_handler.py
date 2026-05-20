
from datetime import datetime, timedelta
from jose import jwt

SECRET_KEY = "secret123"

# Decode expects HS256, but encode will use HS512 (wrong on purpose)
ALGORITHM = "HS256"

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=60)
    to_encode.update({"exp": int(expire.timestamp())})

    # WRONG ON PURPOSE → HS512
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm="HS512")
    return encoded_jwt

def verify_access_token(token: str):
    # Decode expects HS256 → mismatch
    payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    return payload
