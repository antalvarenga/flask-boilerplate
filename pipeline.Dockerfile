FROM ubuntu:18.04

RUN apt-get update

RUN apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip awscli

RUN apt-get install -y curl docker.io

RUN curl -L https://raw.githubusercontent.com/docker/compose-cli/main/scripts/install/install_linux.sh | sh

WORKDIR /app

COPY . /app

CMD ["python3"]