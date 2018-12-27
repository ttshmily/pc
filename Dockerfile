FROM python:3.6

MAINTAINER Fang Chao <ttshmilyfc@qq.com>

COPY pc/ book/ requirements.txt manage.py uwsgi.ini /usr/src/

WORKDIR /usr/src

EXPOSE 9005

RUN pip install --no-cache-dir -r requirements.txt

CMD ["--ini", "uwsgi.ini"]

ENTRYPOINT ["uwsgi"]