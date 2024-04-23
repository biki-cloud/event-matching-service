from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from datetime import datetime


def signup_view(request):
    if request.method == 'POST':

        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(to='/accounts/profile/')

    else:
        form = SignupForm()

    param = {
        'form': form
    }

    return render(request, 'accounts/signup.html', param)


def login_view(request):
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
def profile_view(request):
    user = request.user

    params = {
        'age': user.get_age(),
    }

    return render(request, 'accounts/profile.html', params)
