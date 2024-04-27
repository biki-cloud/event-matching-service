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
python manage.py shell << EOF
from django.contrib.auth import get_user_model
from accounts.models import OrganizerProfile
from events.models import Event

User = get_user_model()
user = User.objects.create_user(username='organizer1', email='organizer1@example.com', password='password')
print("#" * 100)
print("created user")
print(user.__dict__)

print("#" * 100)
print("created organizer profile")
organizer_profile = OrganizerProfile.objects.create(user=user)
print(organizer_profile.__dict__)

# イベントを作成する
event = Event.objects.create(
    name='Sample Event',
    date='2024-04-30',
    location='Sample Location',
    description='Sample Description',
    organizer=organizer_profile
)
print("#" * 100)
print("created event")
print(event.__dict__)


User = get_user_model()
user = User.objects.create_user(username='organizer2', email='organizer2@example.com', password='password')
print("#" * 100)
print("created user")
print(user.__dict__)

print("#" * 100)
print("created organizer profile")
organizer_profile = OrganizerProfile.objects.create(user=user)
print(organizer_profile.__dict__)

# イベントを作成する
event = Event.objects.create(
    name='test Event',
    date='2024-04-30',
    location='Sample Location',
    description='Sample Description',
    organizer=organizer_profile
)
print("#" * 100)
print("created event")
print(event.__dict__)
EOF