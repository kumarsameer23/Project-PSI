import os
import uuid
import shutil
from fastapi import APIRouter, UploadFile, File, Depends
from app.core.security import get_current_user
from app.services.pdf_service import extract_text_from_pdf
from app.services.media_service import transcribe_media
from app.services.vector_service import create_embeddings
from app.core.database import db

router = APIRouter(prefix="/upload", tags=["Upload"])


@router.post("/")
async def upload_file(file: UploadFile = File(...), user=Depends(get_current_user)):
    path = f"uploads/{file.filename}"
    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    file_id = str(uuid.uuid4())

    if file.filename.endswith(".pdf"):
        text = extract_text_from_pdf(path)
        segments = []
    else:
        text, segments = transcribe_media(path)

    db.files.insert_one({
        "file_id": file_id,
        "filename": file.filename,
        "user_email": user["email"],
        "text": text,
        "segments": segments
    })

    create_embeddings(file_id, text, segments)
    os.makedirs("uploads", exist_ok=True)

    return {"file_id": file_id}
