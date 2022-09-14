FROM python:3.10
ENV PYTHONUNBUFFERED 1
ENV DJANGO_DEBUG=True

WORKDIR /app

ADD . . 

RUN pip install -U pip && pip install -r requirements.txt 

