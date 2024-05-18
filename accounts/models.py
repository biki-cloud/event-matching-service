from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class CustomUser(AbstractUser):
    """拡張ユーザーモデル"""

    class Meta:
        db_table = "custom_user"

    ROLE_CHOICES = (
        ("organizer", "イベント主催者"),
        ("vendor", "イベント出店者"),
        ("customer", "イベント参加者"),
    )

    role_type = models.CharField("アカウント種別", max_length=20, choices=ROLE_CHOICES)

    @property
    def organizer(self):
        # ログインしているユーザを外部キーとして持つorganizer profileが存在する場合、そのorganizer profileを返す
        return self.organizer_profile if hasattr(self, "organizer_profile") else None

    @property
    def vendor(self):
        # ログインしているユーザを外部キーとして持つvendor profileが存在する場合、そのvendor profileを返す
        return self.vendor_profile if hasattr(self, "vendor_profile") else None
