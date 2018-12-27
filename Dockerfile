FROM python:3.6

MAINTAINER Fang Chao <ttshmilyfc@qq.com>

COPY pc/ book/ requirements.txt manage.py uwsgi.ini /usr/src/

WORKDIR /usr/src

EXPOSE 9005

RUN pip install -r requirements.txt && \
    pwd && ls -l && \
    python manage.py makemigrations && \
    python manage.py migrate

CMD ["--ini", "uwsgi.ini"]

ENTRYPOINT ["uwsgi"]