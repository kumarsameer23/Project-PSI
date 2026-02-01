import uuid
from app.core.database import db
from app.services.pdf_service import extract_text_from_pdf
from app.services.media_service import save_media_file, transcribe_media
from app.services.vector_service import create_embeddings


async def process_file(file, user_email):
    file_id = str(uuid.uuid4())

    filename = file.filename.lower()

    # -------- PDF --------
    if filename.endswith(".pdf"):
        text = extract_text_from_pdf(file)

        db.files.insert_one({
            "file_id": file_id,
            "filename": file.filename,
            "user_email": user_email,
            "text": text,
            "type": "pdf"
        })

        create_embeddings(file_id, text)

    # -------- AUDIO / VIDEO --------
    elif filename.endswith((".mp3", ".wav", ".m4a", ".mp4", ".mov")):
        path = save_media_file(file)
        text, segments = transcribe_media(path)

        db.files.insert_one({
            "file_id": file_id,
            "filename": file.filename,
            "user_email": user_email,
            "text": text,
            "segments": segments,
            "type": "media"
        })

        create_embeddings(file_id, text)

    else:
        raise ValueError("Unsupported file type")

    return file_id
