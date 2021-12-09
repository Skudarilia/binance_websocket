FROM python:3.8-alpine
MAINTAINER Skudar Ilia <skudarilya@gmail.com>
WORKDIR /code
COPY . .
RUN apk add --update gcc
RUN apk add --update libffi-dev
RUN apk add --update musl-dev
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD [ "python", "-u", "./src/work.py" ]
