from django.shortcuts import render, redirect
from .forms import (
    LoginForm,
    OrganizerProfileForm,
    VendorProfileForm,
    EditForm
)
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import OrganizerProfile, VendorProfile
from allauth.account.views import LoginView, SignupView

import logging

logger = logging.getLogger('myapp')

def accounts_home(request):
    return render(request, 'accounts/accounts_home.html')


class CustomSignupView(SignupView):
    template_name = 'account/signup.html'

    def form_valid(self, form):
        user = form.save(self.request)
        # organizerモデルがフォームで入力されていれば保存
        organizer_profile_form = OrganizerProfileForm(self.request.POST, instance=user.organizer_profile)
        if organizer_profile_form.is_valid():
            organizer_profile_form.save()
        
        # vendorモデルがフォームで入力されていれば保存
        vendor_profile_form = VendorProfileForm(self.request.POST, instance=user.vendor_profile)
        if vendor_profile_form.is_valid():
            vendor_profile_form.save()

        return super().form_valid(form)


class CustomLoginView(LoginView):
    template_name = 'account/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['organizer_form'] = OrganizerProfileForm()
        context['vendor_form'] = VendorProfileForm()
        context['test'] = 'xxxx'
        return context

@login_required
def profile(request):
    user = request.user

    organizer = OrganizerProfile.objects.all().filter(user=user).first()
    vendor = VendorProfile.objects.all().filter(user=user).first()

    params = {
        'organizer': organizer,
        'vendor': vendor,
    }

    return render(request, 'accounts/profile.html', params)


@login_required
def profile_edit(request):
    user = request.user

    organizer = OrganizerProfile.objects.filter(user=user).first()
    vendor = VendorProfile.objects.filter(user=user).first()

    organizer_form = OrganizerProfileForm(request.POST or None, instance=organizer)
    vendor_form = VendorProfileForm(request.POST or None, instance=vendor)
    edit_form = EditForm(request.POST or None, request.FILES or None, instance=user)

    if request.method == "POST":
        if organizer_form.is_valid():
            organizer = organizer_form.save(commit=False)
            organizer.user = user
            organizer.save()

        if vendor_form.is_valid():
            vendor = vendor_form.save(commit=False)
            vendor.user = user
            vendor.save()

        if edit_form.is_valid():
            edit_form.save()

        return redirect(to='/accounts/profile/')

    params = {
        'organizer_form': organizer_form,
        'vendor_form': vendor_form,
        'form': edit_form,
    }

    return render(request, 'accounts/profile_edit.html', params)


def user_logout(request):
    logout(request)
    return redirect(to='/accounts/login/')
