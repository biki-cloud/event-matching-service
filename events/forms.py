from django import forms

from .models import Event
from .models import EventApplication


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            "name",
            "date",
            "location",
            "description",
            "image",
            "status",
            "is_finished",
            "type",
        ]


class EventApplicationForm(forms.ModelForm):
    class Meta:
        model = EventApplication
        fields = ["message"]
