FROM python:3.9

WORKDIR /service

COPY requirements.txt /service/
COPY . /service/

RUN pip install -r /service/requirements.txt

RUN adduser --disabled-password service-user

USER service-user
