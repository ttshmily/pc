FROM python:3.6

MAINTAINER Fang Chao <ttshmilyfc@qq.com>

COPY pc/ /usr/src/
COPY book/ /usr/src/
COPY manage.py /usr/src/
COPY requirements.txt /usr/src/
COPY uwsgi.ini /usr/src/

WORKDIR /usr/src

RUN pip install --no-cache-dir -r requirements.txt

CMD ["--ini", "uwsgi.ini"]

EXPOSE 9005

ENTRYPOINT ["uwsgi"]