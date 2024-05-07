from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm, OrganizerProfileForm, VendorProfileForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import OrganizerProfile, VendorProfile


def accounts_home(request):
    return render(request, 'accounts/accounts_home.html')


def signup(request):
    form = SignupForm(request.POST or None)
    organizer_profile_form = OrganizerProfileForm(request.POST or None)
    vendor_profile_form = VendorProfileForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        # Userモデル処理
        user = form.save(commit=False)
        user.save()

        # organizerモデルがフォームで入力されていれば保存
        if organizer_profile_form.is_valid():
            organizer_profile = organizer_profile_form.save(commit=False)
            organizer_profile.user = user
            organizer_profile.save()

        # vendorモデルがフォームで入力されていれば保存
        if vendor_profile_form.is_valid():
            vendor_profile = vendor_profile_form.save(commit=False)
            vendor_profile.user = user
            vendor_profile.save()

        login(request, user)

        return redirect(to='/accounts/profile/')

    context = {
        "form": form,
        "profile_form": organizer_profile_form,
        "vendor_profile_form": vendor_profile_form,
    }
    return render(request, 'accounts/signup.html', context)


def user_login(request):
    if request.method == 'POST':
        next = request.POST.get('next')
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()

            if user:
                login(request, user)
                return redirect(to='/accounts/profile/')

    else:
        form = LoginForm()

    param = {
        'form': form,
    }

    return render(request, 'accounts/login.html', param)


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


def user_logout(request):
    logout(request)
    return redirect(to='/accounts/login/')
