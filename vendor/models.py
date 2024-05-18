from django.db import models

from accounts.models import CustomUser

# Create your models here.


class VendorProfile(models.Model):
    """CustomUserに紐ずくイベント出店者のプロフィールモデル"""

    vendor_name = models.CharField("主催者名", max_length=255, blank=True)
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, related_name="vendor_profile"
    )

    def __str__(self):
        return self.user.email
