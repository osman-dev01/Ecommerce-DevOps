#!/bin/sh

# Exit if any command fails
set -e

echo "Running migrations..."
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Creating superuser if it doesn't exist..."
python manage.py createsuperuser \
  --noinput \
  --username ${DJANGO_SUPERUSER_USERNAME:-admin} \
  --email ${DJANGO_SUPERUSER_EMAIL:-admin@example.com} || true

echo "Starting Gunicorn..."
exec gunicorn ecommerce_project.wsgi:application --bind 0.0.0.0:8000
