import os
from jose import jwt, JWTError
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.core.config import JWT_SECRET

ALGORITHM = "HS256"
security = HTTPBearer()


def create_token(email: str):
    return jwt.encode({"email": email}, JWT_SECRET, algorithm=ALGORITHM)


def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[ALGORITHM])
        return {"email": payload.get("email")}
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
