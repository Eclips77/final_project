FROM python:3.11-slim


RUN mkdir -p /app/services

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY ./services/bds_stage /app/services/

COPY ./tools /app/

CMD [ "python","-m", "services.bds_stage.app.risk_manager" ]
