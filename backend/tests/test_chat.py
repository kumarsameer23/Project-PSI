def test_chat_endpoint(client, auth_headers, monkeypatch):
    fake_chunks = [
        {"text": "AI is great", "start": 0, "end": 5},
        {"text": "Testing is important", "start": 6, "end": 10},
    ]

    monkeypatch.setattr("app.services.chat_service.search_similar",
                        lambda file_id, question: fake_chunks)

    monkeypatch.setattr("app.services.chat_service.ask_llm",
                        lambda context, q: {"answer": "AI is great", "timestamps": [0]})

    res = client.post(
        "/chat/chat/",  # ✅ FIXED PATH
        params={"file_id": "123", "question": "What is AI?"},
        headers=auth_headers
    )

    assert res.status_code == 200
    data = res.json()
    assert data["answer"] == "AI is great"
    assert len(data["timestamps"]) == 1
