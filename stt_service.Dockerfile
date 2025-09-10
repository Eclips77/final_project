
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV FWHISPER_MODEL_DIR=/opt/models

WORKDIR /app

# ARG UID=10001
# RUN adduser \
#     --disabled-password \
#     --gecos "" \
#     --home "/nonexistent" \
#     --shell "/sbin/nologin" \
#     --no-create-home \
#     --uid "${UID}" \
#     appuser

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN python - <<'PY'
from faster_whisper import WhisperModel
WhisperModel("tiny.en")
PY

COPY services/stt_service /app/services/stt_service
COPY tools /app/tools


CMD ["python", "-m", "services.stt_service.app.stt_manager"]