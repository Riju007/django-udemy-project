"""View foe the app users."""
# 3rd party imports
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView

# Local imports
from users.forms import RegisterForm


def register(request):
    """Register an user."""
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Welcome {username}!your account is created')
            return redirect('users:login')
    else:
        form = RegisterForm()

    return render(request, 'users/register.html', {'form': form})


@login_required
def user_profile(request):
    """Display the profile page of the user."""
    return render(request, 'users/profile.html')


class UserLoginView(SuccessMessageMixin, LoginView):
    """View for user login."""

    template_name = 'users/login.html'
    success_message = 'You have logged in successfully.'


class UserLogoutView(LogoutView):
    """View for user logout."""

    template_name = 'users/logout.html'
