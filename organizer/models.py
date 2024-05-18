from django.db import models

from accounts.models import CustomUser


GENDER_CHOICES = (
    ("女性", "女性"),
    ("男性", "男性"),
)

class OrganizerProfile(models.Model):
    """CustomUserに紐ずくイベント主催者のプロフィールモデル"""
    phone = models.CharField("電話番号", max_length=255, blank=True)
    gender = models.CharField("性別", max_length=2, choices=GENDER_CHOICES, blank=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="organizer_profile")

    def __str__(self):
        return self.user.email