from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jwt_handler import create_access_token, verify_access_token

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

@app.post("/login")
def login():
    token = create_access_token({"sub": "mahesh"})
    return {"access_token": token, "token_type": "bearer"}

@app.get("/me")
def me(token: str = Depends(oauth2_scheme)):
    try:
        payload = verify_access_token(token)
        return {"user": payload["sub"]}
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")
