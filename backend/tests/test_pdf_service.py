from app.services.pdf_service import extract_text_from_pdf

def test_pdf_extract(monkeypatch):
    class FakePage:
        def get_text(self):
            return "Hello"

    class FakeDoc:
        def __enter__(self):
            return [FakePage(), FakePage()]
        def __exit__(self, *args):
            pass

    monkeypatch.setattr("app.services.pdf_service.fitz.open", lambda x: FakeDoc())

    text = extract_text_from_pdf("fake.pdf")
    assert text == "HelloHello"
