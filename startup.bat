@echo off
python manage.py collectstatic --noinput
python manage.py migrate
gunicorn --worker-tmp-dir /dev/shm prac1.wsgi
