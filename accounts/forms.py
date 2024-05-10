from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, OrganizerProfile, VendorProfile


class SignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [CustomUser.USERNAME_FIELD] + CustomUser.REQUIRED_FIELDS + ['password1', 'password2', 'role', 'image']


class OrganizerProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['gender'].widget.attrs['class'] = 'form-control'
        self.fields['phone'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = OrganizerProfile
        fields = (
            "gender", "phone"
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


class EditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = [CustomUser.USERNAME_FIELD] + CustomUser.REQUIRED_FIELDS + ['role', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields[CustomUser.USERNAME_FIELD].widget.attrs['class'] = 'form-control'
        # 他のフォームフィールドに対する操作もここで行うことができます
