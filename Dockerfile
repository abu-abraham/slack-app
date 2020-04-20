FROM python:3.8
ADD . /sports
WORKDIR /sports
RUN pip install -r requirements.txt