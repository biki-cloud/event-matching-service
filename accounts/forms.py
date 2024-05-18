import logging

from allauth.account.forms import SignupForm
from django import forms
from django.contrib import messages

from organizer.models import OrganizerProfile
from vendor.models import VendorProfile

from .models import CustomUser

logger = logging.getLogger("myapp")


class CustomSignupForm(SignupForm):
    role_type = forms.ChoiceField(choices=CustomUser.ROLE_CHOICES)

    class Meta:
        model = CustomUser

    def signup(self, request, user):
        # ユーザアカウントの情報を保存
        user.role_type = self.cleaned_data["role_type"]
        user.save()  # まずユーザを保存してから、プロファイルを作成します

        if user.role_type == "organizer":
            # イベント主催者としてプロファイルを作成
            OrganizerProfile.objects.create(user=user)
            messages.success(request, "イベント主催者として登録しました")

        if user.role_type == "vendor":
            # イベント出店者としてプロファイルを作成
            VendorProfile.objects.create(user=user)
            messages.success(request, "イベント出店者として登録しました")

        return user
