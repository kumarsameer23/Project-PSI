def test_transcribe(monkeypatch):
    fake_result = {
        "text": "hello world",
        "segments": [{"start": 0, "end": 1, "text": "hello"}]
    }

    monkeypatch.setattr("app.services.media_service.model.transcribe", lambda x: fake_result)

    from app.services.media_service import transcribe_media
    text, segments = transcribe_media("fake.mp3")

    assert text == "hello world"
    assert segments[0]["text"] == "hello"
