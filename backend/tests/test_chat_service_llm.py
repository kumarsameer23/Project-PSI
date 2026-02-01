from app.services.chat_service import ask_llm


def test_ask_llm_parses_json(monkeypatch):
    class FakeResponse:
        def json(self):
            return {
                "choices": [
                    {"message": {"content": "{'answer': 'Hello', 'timestamps': [0]}"}}
                ]
            }

    monkeypatch.setattr("app.services.chat_service.requests.post",
                        lambda *a, **k: FakeResponse())

    result = ask_llm([{"text": "Hello world"}], "Hi?")
    assert result["answer"] == "Hello"
    assert result["timestamps"] == [0]


def test_ask_llm_fallback_on_bad_json(monkeypatch):
    class FakeResponse:
        def json(self):
            return {
                "choices": [
                    {"message": {"content": "Just text response"}}
                ]
            }

    monkeypatch.setattr("app.services.chat_service.requests.post",
                        lambda *a, **k: FakeResponse())

    result = ask_llm([{"text": "Hello world"}], "Hi?")
    assert result["answer"] == "Just text response"
    assert result["timestamps"] == []
