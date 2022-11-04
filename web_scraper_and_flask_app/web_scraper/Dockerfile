FROM python:3.8

USER root

RUN apt-get update \
    && apt-get install -y apt-transport-https \
    && apt-get -y install gcc make \
    && rm -rf /var/lib/apt/lists/*s \
    && apt-get -y install xdg-utils \
    && apt-get -y install libxkbcommon0 \
    && apt-get -y install libxfixes3 \
    && apt-get -y install libxdamage1 \
    && apt-get -y install libxcomposite1 \
    && apt-get -y install libwayland-client0 \
    && apt-get -y install libnspr4 \
    && apt-get -y install unzip \
    && apt-get -y install libnss3 \
    && apt-get -y install libgbm1 \
    && apt-get -y install libasound2 \
    && apt-get -y install fonts-liberation \
    && apt-get -y install xvfb \
    && apt-get install unzip \
    && apt-get install nano

WORKDIR /home/
COPY  ./application ./application
WORKDIR /home/application/bin

RUN dpkg -i google-chrome-stable_current_amd64.deb
RUN apt --fix-broken install
RUN rm google-chrome-stable_current_amd64.deb

CMD unzip chromedriver_linux64.zip
RUN rm chromedriver_linux64.zip
WORKDIR /home/application
COPY ./requirements.txt ./requirements.txt
RUN pip install --no-cache-dir --upgrade pip

RUN pip install -r requirements.txt


