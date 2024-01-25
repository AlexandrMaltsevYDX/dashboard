#!/bin/bash


python manage.py migrate
mkdir -p staticroot  #the same i settings.py
python manage.py collectstatic
python manage.py spectacular --file staticroot/schema.yaml --validate
exec "$@"
