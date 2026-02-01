from app.services.vector_service import create_embeddings, search_similar

def test_vector_flow(monkeypatch):
    monkeypatch.setattr("app.services.vector_service.model.encode",
                        lambda x: [[0.1]*384]*len(x))

    text = "This is a test. Another sentence."
    segments = [{"start": 0, "end": 1}, {"start": 1, "end": 2}]

    create_embeddings("file1", text, segments)

    results = search_similar("file1", "test")
    assert isinstance(results, list)
    assert len(results) > 0


def test_vector_no_index():
    results = search_similar("missing", "question")
    assert results == []
