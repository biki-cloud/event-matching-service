from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    """拡張ユーザーモデル"""
    class Meta(AbstractUser.Meta):
        db_table = 'custom_user'
    
    ROLE_CHOICES = (
        ('organizer', 'イベント主催者'),
        ('vendor', 'イベント出店者'),
        ('customer', 'イベント参加者')
    )

    role = models.CharField('アカウント種別', max_length=20, choices=ROLE_CHOICES)

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


class VendorProfile(models.Model):
    """CustomUserに紐ずくイベント出店者のプロフィールモデル"""
    vendor_name = models.CharField("主催者名", max_length=255, blank=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="vendor_profile")

    def __str__(self):
        return self.user.email