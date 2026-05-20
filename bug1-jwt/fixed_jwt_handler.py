# fixed code snippet
from datetime import datetime, timedelta
from jose import jwt

SECRET_KEY = "secret123"
ALGORITHM = "HS512"  # FIXED: encode + decode now match

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=60)
    to_encode.update({"exp": int(expire.timestamp())})

    # FIXED: use the same algorithm for encoding
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_access_token(token: str):
    # FIXED: decode using the same algorithm
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return payload