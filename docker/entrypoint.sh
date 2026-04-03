#!/usr/bin/env bash
set -e

# Apply migrations / sync collections in MongoDB
python manage.py migrate --run-syncdb --noinput
python manage.py collectstatic --noinput

exec gunicorn config.wsgi:application --bind 0.0.0.0:8000 --workers 2
