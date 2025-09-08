import os, json
from datetime import datetime
from pathlib import Path
from kafka import KafkaConsumer, KafkaProducer
from faster_whisper import WhisperModel

def transcribe(audio_path: str) -> list:
    model = WhisperModel("small", device="cpu", compute_type="int8")
    segments, info = model.transcribe(audio_path, task="transcribe", beam_size=5, vad_filter=True)
    out = []
    for s in segments:
        out.append({"start": float(s.start), "end": float(s.end), "text_en": s.text})
    return {"language": getattr(info, "language", "en"), "segments": out}

def main():
    pass


if __name__ == "__main__":
    main()
