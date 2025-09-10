FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY ./services/meta_creator /services/app/

COPY ./tools /app/

CMD [ "python","-m", "services.meta_creator.main" ]
