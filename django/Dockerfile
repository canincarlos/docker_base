# FROM python:3.8-slim
# FROM python:3.9
# FROM python:3.8.3-slim-buster 
FROM ubuntu:focal


# https://www.youtube.com/watch?v=jyapP2Yy0AQ
# https://www.youtube.com/watch?v=p28piYY_wv8
# https://stackoverflow.com/questions/35931579/how-can-i-install-lxml-in-docker
# 



ENV PYTHONBUFFERED=1
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONIOENCODING 'utf-8'
ENV LANG 'C.UTF-8'

WORKDIR /django
COPY requirements.txt requirements.txt


# RUN apk add -u zlib-dev jpeg-dev gcc musl-dev
# RUN python3 -m pip install --upgrade pip

RUN apt-get update -qq \
    && apt-get install --no-install-recommends --yes \
# RUN apk update \
#     && apk add --upgrade --no-cache \
        build-essential python3-dev python3-pip python3-setuptools libpq-dev gcc \
    && rm -rf /var/lib/apt/lists/* \
    # && python3 -m pip install --no-cache-dir mysqlclient \
    && apt-get autoremove --purge --yes \
        build-essential

RUN python3 -m pip install --upgrade pip \
    && python3 -m pip install -r requirements.txt

COPY . .   

CMD ["/django/runserver.sh"]