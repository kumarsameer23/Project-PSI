from fastapi import APIRouter
from app.core.security import create_token

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/login")
def login(email: str):
    token = create_token(email)
    return {"access_token": token}
