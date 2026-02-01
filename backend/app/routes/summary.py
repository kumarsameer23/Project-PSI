from fastapi import APIRouter, Depends
from app.core.security import get_current_user
from app.core.database import db

router = APIRouter(prefix="/summary", tags=["Summary"])


@router.get("/{file_id}")
def get_summary(file_id: str, user=Depends(get_current_user)):
    file = db.files.find_one({"file_id": file_id, "user_email": user["email"]})
    if not file:
        return {"summary": "File not found"}

    text = file.get("text", "")
    short = text[:2000]  # simple summary fallback
    return {"summary": short}
