FROM node:7.8.0

RUN mkdir /frontend
WORKDIR /frontend

ADD package.json package-lock.json /frontend/
RUN npm install

ADD . /frontend/
