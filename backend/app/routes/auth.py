from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime, timedelta
from jose import jwt
import os

router = APIRouter()

SECRET_KEY = os.getenv("JWT_SECRET", "supersecret")
ALGORITHM = "HS256"


class AuthRequest(BaseModel):
    email: str
    password: str


@router.post("/register")
def register(user: AuthRequest):
    # For demo — accept any user
    return {"message": "User registered successfully"}


@router.post("/login")
def login(user: AuthRequest):
    expire = datetime.utcnow() + timedelta(hours=10)

    token = jwt.encode(
        {"email": user.email, "exp": expire},
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return {"access_token": token, "token_type": "bearer"}
