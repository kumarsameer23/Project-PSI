import os
from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext
from app.core.db import db

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET = os.getenv("JWT_SECRET")

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(password, hashed):
    return pwd_context.verify(password, hashed)

def create_token(data: dict):
    expire = datetime.utcnow() + timedelta(days=7)
    data.update({"exp": expire})
    return jwt.encode(data, SECRET, algorithm="HS256")

def register_user(email, password):
    if db.users.find_one({"email": email}):
        return None
    hashed = hash_password(password)
    db.users.insert_one({"email": email, "password": hashed})
    return True

def login_user(email, password):
    user = db.users.find_one({"email": email})
    if not user or not verify_password(password, user["password"]):
        return None
    return create_token({"email": email})
