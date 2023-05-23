FROM python:3.11.3-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk add  --no-cache --update \
    bash \
    && rm -rf /var/cache/apk/*

RUN mkdir app
WORKDIR app
COPY . /app

RUN pip3 install --upgrade pip \
    && pip3 install -r requirements.txt

EXPOSE 8000
