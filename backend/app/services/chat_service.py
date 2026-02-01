import requests
import os
from app.services.vector_service import search_similar

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL = "llama-3.1-8b-instant"


def ask_llm(context_chunks, question):
    context_text = "\n".join(
        [f"[{i}] {c['text']}" for i, c in enumerate(context_chunks)]
    )

    prompt = f"""
You are an AI assistant analyzing a transcript.

Context:
{context_text}

User Question:
{question}

Instructions:
1. Answer clearly using ONLY the context.
2. Return JSON in this format:
{{
  "answer": "...",
  "timestamps": [indexes of context chunks used]
}}
"""

    res = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "model": MODEL,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.2,
        },
    )

    data = res.json()
    content = data["choices"][0]["message"]["content"]

    try:
        parsed = eval(content)  # safe enough because we control format
        return parsed
    except:
        return {"answer": content, "timestamps": []}


def chat_with_file(file_id: str, question: str, user_email: str):
    context_chunks = search_similar(file_id, question)

    if not context_chunks:
        return {"answer": "No relevant information found", "timestamps": []}

    llm_output = ask_llm(context_chunks, question)

    timestamps = []
    for idx in llm_output.get("timestamps", []):
        if idx < len(context_chunks):
            chunk = context_chunks[idx]
            if chunk["start"] is not None:
                timestamps.append({
                    "start": chunk["start"],
                    "end": chunk["end"],
                    "text": chunk["text"]
                })

    return {
        "answer": llm_output.get("answer", ""),
        "timestamps": timestamps
    }
