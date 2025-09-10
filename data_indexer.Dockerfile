FROM python:3.11-slim

RUN mkdir -p /app/services


WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY ./services/data_indexer /app/services/

COPY ./tools /app/

CMD [ "python","-m", "services.data_indexer.app.manager" ]
