from allauth.account.forms import SignupForm
from django import forms
from .models import CustomUser
from organizer.models import OrganizerProfile
import logging
from django.contrib import messages


logger = logging.getLogger('myapp')


class CustomSignupForm(SignupForm):
    role_type = forms.ChoiceField(choices=CustomUser.ROLE_CHOICES)

    class Meta:
        model = CustomUser

    def signup(self, request, user):
        # ユーザアカウントの情報を保存
        user.role_type = self.cleaned_data['role_type']
        user.save()  # まずユーザを保存してから、プロファイルを作成します

        if user.role_type == 'organizer':
            organizer_profile = OrganizerProfile.objects.create(user=user)
            messages.success(request, 'イベント主催者として登録しました')

        return user