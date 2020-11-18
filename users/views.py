"""View foe the app users."""
# 3rd party imports
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


def register(request):
    """Register an user."""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Welcome {username}!your account is created')
            return redirect('food:home')
    else:
        form = UserCreationForm()

    return render(request, 'users/register.html', {'form': form})
