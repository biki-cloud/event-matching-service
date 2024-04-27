from django.contrib.auth import get_user_model
from accounts.models import OrganizerProfile
from events.models import Event

# ------------------------------------------------------------
print("#" * 100)
print("create organizer1")
User = get_user_model()
user = User.objects.create_user(username='organizer1', email='organizer1@example.com', password='password')
print(user.__dict__)
print("*" * 50)
organizer_profile = OrganizerProfile.objects.create(user=user)
print(organizer_profile.__dict__)

print("create event")
event = Event.objects.create(
    name='Sample Event',
    date='2024-04-30',
    location='Sample Location',
    description='Sample Description',
    organizer=organizer_profile
)
print(event.__dict__)


# ------------------------------------------------------------
print("#" * 100)

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
