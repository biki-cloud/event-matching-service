import json
from django.contrib.auth import get_user_model
from accounts.models import OrganizerProfile
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

# ユーザーとイベントを作成するためのforループ
for entry in data:
    # ユーザーを作成
    User = get_user_model()
    user = User.objects.create_user(
        username=entry['username'],
        email=entry['email'],
        password=entry['password']
    )
    print("#" * 100)
    print("created user")
    print(user.__dict__)

    # OrganizerProfileを作成
    organizer_profile = OrganizerProfile.objects.create(user=user)
    print("#" * 100)
    print("created organizer profile")
    print(organizer_profile.__dict__)

    # イベントを作成
    for event_info in entry['events']:
        event = Event.objects.create(
            name=event_info['event_name'],
            date=event_info['event_date'],
            location=event_info['event_location'],
            description=event_info['event_description'],
            organizer=organizer_profile
        )
        print("#" * 100)
        print("created event")
        print(event.__dict__)
