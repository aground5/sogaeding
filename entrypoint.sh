#!/bin/sh

python manage.py collectstatic --noinput --clear
python manage.py migrate
gunicorn --config gunicorn-cfg.py config.wsgi