from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm, ProfileForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


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
    }

    return render(request, 'accounts/profile.html', params)


def new(request):
    form = SignupForm(request.POST or None)
    profile_form = ProfileForm(request.POST or None)

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

        return redirect(to='/accounts/profile/')

    context = {
        "form": form,
        "profile_form": profile_form,
    }
    return render(request, 'accounts/form.html', context)