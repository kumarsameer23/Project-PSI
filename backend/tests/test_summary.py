def test_summary_found(client, auth_headers, monkeypatch):
    fake_file = {"text": "A" * 3000}

    class FakeFiles:
        def find_one(self, query):
            return fake_file

    monkeypatch.setattr("app.routes.summary.db.files", FakeFiles())

    res = client.get("/summary/abc123", headers=auth_headers)
    assert res.status_code == 200
    assert len(res.json()["summary"]) == 2000


def test_summary_not_found(client, auth_headers, monkeypatch):
    class FakeFiles:
        def find_one(self, query):
            return None

    monkeypatch.setattr("app.routes.summary.db.files", FakeFiles())

    res = client.get("/summary/abc123", headers=auth_headers)
    assert res.status_code == 200
    assert res.json()["summary"] == "File not found"
