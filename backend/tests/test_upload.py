import io

def test_upload_pdf(client, auth_headers, monkeypatch):
    monkeypatch.setattr("app.routes.upload.extract_text_from_pdf",
                        lambda path: "PDF content")

    monkeypatch.setattr("app.routes.upload.create_embeddings",
                        lambda file_id, text, segments: None)

    fake_pdf = io.BytesIO(b"%PDF-1.4 fake content")

    res = client.post(
        "/upload/",
        files={"file": ("test.pdf", fake_pdf, "application/pdf")},
        headers=auth_headers
    )

    assert res.status_code == 200
    assert "file_id" in res.json()


def test_upload_media(client, auth_headers, monkeypatch):
    monkeypatch.setattr("app.routes.upload.transcribe_media",
                        lambda path: ("audio text", [{"start": 0, "end": 1, "text": "audio"}]))

    monkeypatch.setattr("app.routes.upload.create_embeddings",
                        lambda file_id, text, segments: None)

    fake_audio = io.BytesIO(b"fake audio")

    res = client.post(
        "/upload/",
        files={"file": ("test.mp3", fake_audio, "audio/mpeg")},
        headers=auth_headers
    )

    assert res.status_code == 200
    assert "file_id" in res.json()
