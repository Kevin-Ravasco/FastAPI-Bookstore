FROM python:3.9.6-slim

ENV PYTHONUNBUFFERED=1

# RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY . /app
COPY requirements.txt requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
EXPOSE 8000