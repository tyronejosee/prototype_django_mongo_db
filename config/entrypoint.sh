#!/bin/sh

set -e

echo "Starting Django with Mongo..."
python manage.py runserver 0.0.0.0:8000
