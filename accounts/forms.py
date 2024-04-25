from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, Organizer


class SignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [CustomUser.USERNAME_FIELD] + CustomUser.REQUIRED_FIELDS + ['password1', 'password2']


class OrganizerSignupForm(UserCreationForm):
    class Meta:
        model = Organizer
        fields = [Organizer.USERNAME_FIELD] + Organizer.REQUIRED_FIELDS + ['password1', 'password2']

class LoginForm(AuthenticationForm):
    pass
