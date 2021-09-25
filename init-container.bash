#!/bin/bash
echo "Start Init Container script"
echo "Running Makemigrations"
python manage.py makemigrations           # makemigrations database migrations
echo "Running Migrate"
python manage.py migrate                  # Apply database migrations
echo "Running Collectstatic"
python manage.py collectstatic --noinput  # Collect static files
echo "All services are configured and ready to run!"
exec "$@"