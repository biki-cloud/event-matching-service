import json
from django.contrib.auth import get_user_model
from accounts.models import OrganizerProfile, VendorProfile
from events.models import Event

# JSON形式のデータを定義
data = [
    {
        "username": "organizer1",
        "email": "organizer1@example.com",
        "password": "password",
        "events": [
            {
                "event_name": "Sample Event 1",
                "event_date": "2024-04-30",
                "event_location": "Sample Location 1",
                "event_description": "Sample Description 1"
            },
            {
                "event_name": "Sample Event 2",
                "event_date": "2024-05-01",
                "event_location": "Sample Location 2",
                "event_description": "Sample Description 2"
            }
        ]
    },
    {
        "username": "organizer2",
        "email": "organizer2@example.com",
        "password": "password",
        "events": [
            {
                "event_name": "Sample Event 3",
                "event_date": "2024-05-02",
                "event_location": "Sample Location 3",
                "event_description": "Sample Description 3"
            },
            {
                "event_name": "Sample Event 4",
                "event_date": "2024-05-03",
                "event_location": "Sample Location 4",
                "event_description": "Sample Description 4"
            }
        ]
    }
]

events = []

# ユーザーとイベントを作成するためのforループ
for entry in data:
    print("#" * 100)
    # ユーザーを作成
    User = get_user_model()
    user = User.objects.create_user(
        username=entry['username'],
        email=entry['email'],
        password=entry['password']
    )
    print("*" * 50)
    print("created user")
    print(user.__dict__)

    # OrganizerProfileを作成
    organizer_profile = OrganizerProfile.objects.create(user=user)
    print("*" * 50)
    print("created organizer profile")
    print(organizer_profile.__dict__)



    # イベントを作成
    for idx, event_info in enumerate(entry['events']):
        event = Event.objects.create(
            name=event_info['event_name'],
            date=event_info['event_date'],
            location=event_info['event_location'],
            description=event_info['event_description'],
            organizer=organizer_profile
        )
        events.append(event)
        print("*" * 50)
        print("created event " + str(idx + 1))
        print(event.__dict__)
        print(event.vendors.all())

# Vendorを作成
User = get_user_model()
user = User.objects.create_user(
    username='vendor1',
    email='vendor1@example.com',
    password='password'
)
vendor_profile = VendorProfile.objects.create(user=user, vendor_name="Sample Vendor")
print("*" * 50)
print("created vendor profile")
print(vendor_profile.__dict__)
for event in events:
    event.vendors.add(vendor_profile)
    print("*" * 50)
    print("added vendor to event")
    print(event.vendors.all())