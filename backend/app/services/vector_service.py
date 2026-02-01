import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from app.core.database import db

model = SentenceTransformer("all-MiniLM-L6-v2")
dimension = 384

index_store = {}
chunk_store = {}


def create_embeddings(file_id: str, text: str, segments=None):
    chunks = text.split(". ")
    embeddings = model.encode(chunks)

    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings).astype("float32"))

    index_store[file_id] = index
    chunk_store[file_id] = {
        "chunks": chunks,
        "segments": segments or []
    }


def search_similar(file_id: str, question: str, top_k: int = 5):
    if file_id not in index_store:
        return []

    question_embedding = model.encode([question])
    D, I = index_store[file_id].search(
        np.array(question_embedding).astype("float32"), top_k
    )

    results = []
    stored = chunk_store[file_id]
    chunks = stored["chunks"]
    segments = stored["segments"]

    for idx in I[0]:
        if idx < len(chunks):
            seg = segments[idx] if idx < len(segments) else None
            results.append({
                "text": chunks[idx],
                "start": seg.get("start") if seg else None,
                "end": seg.get("end") if seg else None
            })

    return results
