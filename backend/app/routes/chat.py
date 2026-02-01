from fastapi import APIRouter, Depends
from app.core.security import get_current_user
from app.services.chat_service import chat_with_file

router = APIRouter(prefix="/chat", tags=["Chat"])


@router.post("/")
def chat(file_id: str, question: str, user=Depends(get_current_user)):
    result = chat_with_file(file_id, question, user["email"])
    return result
