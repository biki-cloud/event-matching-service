from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm, OrganizerProfileForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required


def organizer_signup(request):
    form = SignupForm(request.POST or None)
    profile_form = OrganizerProfileForm(request.POST or None)

    if request.method == "POST" and form.is_valid() and profile_form.is_valid():
        # Userモデル処理
        user = form.save(commit=False)
        user.is_staff = True
        user.save()

        # Profileモデルの処理
        profile = profile_form.save(commit=False)
        profile.user = user
        profile.save()

        login(
            request, user, backend="django.contrib.auth.backends.ModelBackend")

        return redirect(to='/accounts/organizer_profile/')

    context = {
        "form": form,
        "profile_form": profile_form,
    }
    return render(request, 'accounts/organizer_signup.html', context)


def organizer_login(request):
    if request.method == 'POST':
        next = request.POST.get('next')
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()

            if user:
                login(request, user)
                return redirect(to='/accounts/organizer_profile/')

    else:
        form = LoginForm()

    param = {
        'form': form,
    }

    return render(request, 'accounts/organizer_login.html', param)


@login_required
def organizer_profile(request):
    user = request.user

    params = {
    }

    return render(request, 'accounts/organizer_profile.html', params)


def organizer_logout(request):
    logout(request)
    return redirect(to='/accounts/organizer_login/')


def accounts_home(request):
    return render(request, 'accounts/accounts_home.html')
