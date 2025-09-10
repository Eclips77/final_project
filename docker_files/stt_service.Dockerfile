FROM python:3.11-slim

WORKDIR /app
ENV FWHISPER_MODEL_DIR=/opt/models

COPY requirements.txt ./


RUN pip install --no-cache-dir -r requirements.txt

RUN python - <<'PY'
from faster_whisper import WhisperModel
import os
WhisperModel("tiny.en")
PY

COPY services/tts_service /app/services
COPY tools /app/tools

CMD ["python", "-m", "services.app.stt_manager"]