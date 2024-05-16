from allauth.account.forms import SignupForm
from django import forms
from .models import CustomUser

class CustomSignupForm(SignupForm):
    role = forms.ChoiceField(choices=CustomUser.ROLE_CHOICES)

    class Meta:
        model = CustomUser

    def signup(self, request, user):
        # ユーザアカウントの情報を保存
        user.role = self.cleaned_data['role']
        user.save()

        return user