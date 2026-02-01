def test_register(client):
    res = client.post("/auth/register", json={
        "email": "a@test.com",
        "password": "123"
    })
    assert res.status_code == 200
    assert "message" in res.json()


def test_login_returns_token(client):
    res = client.post("/auth/login", json={
        "email": "a@test.com",
        "password": "123"
    })
    data = res.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"
