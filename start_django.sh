#!/bin/sh

python3 manage.py migrate

python3 manage.py collectstatic --noinput

uwsgi --ini uwsgi.ini && sleep 5 && tail -f uwsgiServer.log
