
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV FWHISPER_MODEL_DIR=/opt/models

RUN mkdir -p /app/services


WORKDIR /app


RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN python - <<'PY'
from faster_whisper import WhisperModel
WhisperModel("tiny.en")
PY

COPY ./services/stt_service app/services/
COPY tools /app/tools


CMD ["python", "-m", "services.stt_service.app.stt_manager"]