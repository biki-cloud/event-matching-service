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



class VendorProfile(models.Model):
    """CustomUserに紐ずくイベント出店者のプロフィールモデル"""
    vendor_name = models.CharField("主催者名", max_length=255, blank=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="vendor_profile")

    def __str__(self):
        return self.user.email