#!/bin/sh

# Reset the database
rm accounts/migrations/0*.py
rm events/migrations/0*.py

rm db.sqlite3

# Create new migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser
# python manage.py createsuperuser