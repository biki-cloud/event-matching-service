import json
from django.contrib.auth import get_user_model
from accounts.models import OrganizerProfile, VendorProfile
from events.models import Event

# JSONファイルを読み込む
with open('init_data.json') as f:
    data = json.load(f)

User = get_user_model()

# ユーザーとイベントを作成するためのforループ
for entry in data['organizers']:
    # ユーザーを作成
    user = User.objects.create_user(
        username=entry['username'],
        email=entry['email'],
        password=entry['password'],
        role='イベント主催者'
    )

    # OrganizerProfileを作成
    organizer_profile = OrganizerProfile.objects.create(
        user=user,
        phone=entry['phone'],
        gender=entry['gender']
    )

    # イベントを作成
    for event_info in entry['create_events']:
        Event.objects.create(
            name=event_info['event_name'],
            date=event_info['event_date'],
            location=event_info['event_location'],
            description=event_info['event_description'],
            organizer=organizer_profile
        )

# Vendorを作成
for entry in data['vendors']:
    user = User.objects.create_user(
        username=entry['username'],
        email=entry['email'],
        password=entry['password'],
        role='イベント出店者'
    )
    vendor_profile = VendorProfile.objects.create(
        user=user,
        vendor_name=entry['vendor_name']
    )

    # イベントにvendorを追加
    for event_name in entry['apply_events']:
        event = Event.objects.get(name=event_name)
        event.vendors.add(vendor_profile)