
FROM python:3.10-slim

WORKDIR /code

RUN apt-get update && apt-get install -y --no-install-recommends --no-install-suggests build-essential default-libmysqlclient-dev && pip install --no-cache-dir --upgrade pip

RUN python -m venv /opt/venv

COPY ./requirements.txt /code

RUN /opt/venv/bin/pip install pip --upgrade && /opt/venv/bin/pip install -r /code/requirements.txt --no-cache-dir 

COPY . /code

RUN chmod +x ./entrypoint.sh
