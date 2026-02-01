from app.services.chat_service import chat_with_file


def test_chat_no_context(monkeypatch):
    monkeypatch.setattr("app.services.chat_service.search_similar", lambda a, b: [])
    result = chat_with_file("id", "question", "email@test.com")
    assert result["answer"] == "No relevant information found"


def test_chat_with_context(monkeypatch):
    chunks = [{"text": "hello", "start": 0, "end": 1}]

    monkeypatch.setattr("app.services.chat_service.search_similar", lambda a, b: chunks)
    monkeypatch.setattr("app.services.chat_service.ask_llm",
                        lambda c, q: {"answer": "hello", "timestamps": [0]})

    result = chat_with_file("id", "question", "email@test.com")
    assert result["answer"] == "hello"
    assert result["timestamps"][0]["start"] == 0
