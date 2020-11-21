"""View foe the app users."""
# 3rd party imports
from django.shortcuts import render, redirect
from django.contrib import messages
from users.forms import RegisterForm
from django.contrib.auth.decorators import login_required


def register(request):
    """Register an user."""
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Welcome {username}!your account is created')
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'users/register.html', {'form': form})


@login_required
def user_profile(request):
    """Display the profile page of the user."""
    return render(request, 'users/profile.html')
