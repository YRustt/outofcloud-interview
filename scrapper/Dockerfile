FROM python:3.7

ENV PYTHONUNBUFFERED 1

RUN mkdir /scrapper
WORKDIR /scrapper

ADD requirements.txt /scrapper/
RUN pip install -r requirements.txt

ADD . /scrapper/