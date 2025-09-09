FROM python:3.8-slim

WORKDIR /usr/src/app

COPY requirements.txt ./

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY ./services/data_indexer /usr/src/app/

COPY ./tools /usr/src/app/

CMD [ "python","-m", "./data_indexer/src.manager" ]
