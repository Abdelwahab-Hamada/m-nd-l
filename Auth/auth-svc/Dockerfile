FROM python:3.10-slim

RUN apt-get update \
    && apt-get install -y --no-install-recommends --no-install-suggests \
    build-essential default-libmysqlclient-dev \
    && pip install --no-cache-dir --upgrade pip

WORKDIR /code
COPY ./requirements.txt /code
RUN pip install -r /code/requirements.txt --no-cache-dir
COPY . /code

# RUN python manage.py migrate 

