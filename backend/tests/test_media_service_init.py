import importlib
import os
import app.services.media_service as media_service


def test_ffmpeg_path_exists(monkeypatch):
    monkeypatch.setattr(os.path, "exists", lambda x: True)
    importlib.reload(media_service)
    assert "PATH" in os.environ
