from django.db import models

# Create your models here.

from django.db import models

from accounts.models import VendorProfile
from organizer.models import OrganizerProfile


class Event(models.Model):
    name = models.CharField(max_length=200,
                            default="")
    date = models.DateField(default="2019-01-01")
    location = models.CharField(max_length=200,
                                default="default location")
    description = models.TextField(default="default description")
    # イベントを作成した主催者を特定するための外部キー
    organizer = models.ForeignKey(OrganizerProfile, on_delete=models.CASCADE)
    # イベントに参加するベンダーを特定するための多対多の関係
    vendors = models.ManyToManyField(VendorProfile, blank=True, related_name="vendors")
    image = models.ImageField("プロフィール画像", upload_to='images/', blank=True, null=True)
    # 既存のフィールドは省略
    STATUS_CHOICES = (
        ('draft', '下書き'),
        ('published', '公開済み')
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    is_finished = models.BooleanField(default=False)
    EVENT_TYPE_CHOICES = (
        ('festival', '祭り'),
        ('concert', 'コンサート'),
        ('sports', 'スポーツ'),
        ('other', 'その他'),
    )
    type = models.CharField(max_length=10, choices=EVENT_TYPE_CHOICES, default='festival')

    def __str__(self):
        return self.name

class EventApplication(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='applications')
    vendor = models.ForeignKey(VendorProfile, on_delete=models.CASCADE, related_name='applications')
    message = models.TextField(default="default message")
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.vendor} application for {self.event}"
