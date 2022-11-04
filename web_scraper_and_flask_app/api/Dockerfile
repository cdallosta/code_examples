FROM python:3.8
RUN apt-get update \
    && apt-get -y upgrade \
    && apt-get install -y  tzdata
ENV TZ="America/Los_Angeles"
WORKDIR /home/
COPY ./application ./application
WORKDIR /home/application
COPY ./requirements.txt  ./requirements.txt
RUN pip install --no-cache-dir --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5000
