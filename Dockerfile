FROM python:3.6

MAINTAINER Fang Chao <ttshmilyfc@qq.com>

COPY . /usr/src/

WORKDIR /usr/src

EXPOSE 9005

RUN pip install -r requirements.txt && \
    pwd && ls -l && \
    rm -rf ~/.cache/pip

ENTRYPOINT ./start-django.sh