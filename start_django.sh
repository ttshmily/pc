#! /bin/sh

python manage.py makemigrations

python manage.py migrate

uwsgi --ini /root/docker-django-test-uwsgi.ini
