from fastapi import HTTPException
from app.core.security import get_current_user


class FakeCreds:
    def __init__(self, token):
        self.credentials = token


def test_invalid_token():
    bad_creds = FakeCreds("invalid.token.here")

    try:
        get_current_user(bad_creds)
    except HTTPException as e:
        assert e.status_code == 401
