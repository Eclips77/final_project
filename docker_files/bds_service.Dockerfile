FROM python:311-slim

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY ./services/bds_stage /services/app/

COPY ./tools /app/

CMD [ "python","-m", "services.bds_stage.app.risk_manager" ]
