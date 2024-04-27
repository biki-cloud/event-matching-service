#!/bin/sh

# Reset the database
rm accounts/migrations/0*.py
rm events/migrations/0*.py

rm db.sqlite3

# Create new migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser
export DJANGO_SUPERUSER_USERNAME=admin
export DJANGO_SUPERUSER_EMAIL=admin@example.com
export DJANGO_SUPERUSER_PASSWORD=$(cat password.txt)
python manage.py createsuperuser --noinput

# Create regular user with OrganizerProfile
python manage.py shell < init_db.py