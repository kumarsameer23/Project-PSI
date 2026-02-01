import whisper

# Load Whisper model once
model = whisper.load_model("base")


def transcribe_media(file_path: str):
    result = model.transcribe(file_path)

    full_text = result["text"]

    segments = [
        {
            "start": seg["start"],
            "end": seg["end"],
            "text": seg["text"]
        }
        for seg in result["segments"]
    ]

    return full_text, segments
