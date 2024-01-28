#!/bin/bash
echo "Waiting for postgres..."

#while ! nc -z "$POSTGRES_HOST" 5432; do
#  sleep 0.1
#done
#
#echo "PostgreSQL started"

python manage.py migrate
mkdir -p staticroot  #the same i settings.py
python manage.py collectstatic --noinput
python manage.py spectacular --file staticroot/schema.yaml --validate
exec "$@"
