from django.db import models

# Create your models here.

from django.db import models

from accounts.models import OrganizerProfile, VendorProfile


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
        ('published', '公開済み'),
        ('deleted', '削除済み'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    is_finished = models.BooleanField(default=False)

    def __str__(self):
        return self.name
