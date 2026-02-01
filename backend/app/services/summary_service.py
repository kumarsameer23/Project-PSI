import requests
from app.core.config import OPENAI_API_KEY
from app.core.database import db


def generate_summary(file_id, user_email):
    file = db.files.find_one({"file_id": file_id})
    text = file["text"][:4000]

    url = "https://api.openai.com/v1/chat/completions"
    headers = {"Authorization": f"Bearer {OPENAI_API_KEY}"}
    data = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": "Summarize the following"},
            {"role": "user", "content": text}
        ]
    }

    response = requests.post(url, headers=headers, json=data)
    return {"summary": response.json()["choices"][0]["message"]["content"]}
