from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, OrganizerProfile, VendorProfile


class SignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [CustomUser.USERNAME_FIELD] + CustomUser.REQUIRED_FIELDS + ['password1', 'password2']


class OrganizerProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['gendar'].widget.attrs['class'] = 'form-control'
        self.fields['phone'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = OrganizerProfile
        fields = (
            "gendar", "phone"
        )


class VendorProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['vendor_name'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = VendorProfile
        fields = (
            "vendor_name",
        )


class LoginForm(AuthenticationForm):
    pass
