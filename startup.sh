#!/bin/bash

python manage.py collectstatic --noinput --clear
python manage.py migrate
gunicorn --worker-tmp-dir /dev/shm prac1.wsgi
