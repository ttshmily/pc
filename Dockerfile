FROM python:3.6

MAINTAINER Fang Chao <ttshmilyfc@qq.com>

COPY requirements.txt manage.py uwsgi.ini /usr/src/
COPY pc/ /usr/src/pc/
COPY book/ /usr/src/book/

WORKDIR /usr/src

EXPOSE 9005

RUN pip install -r requirements.txt && \
    python manage.py makemigrations && \
    python manage.py migrate && \
    pwd && ls -l

CMD ["--ini", "uwsgi.ini"]

ENTRYPOINT ["uwsgi"]