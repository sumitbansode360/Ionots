from django.shortcuts import render, redirect
from userauths.forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from userauths.models import User

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import UserRegisterForm  # Adjust the import to your form location

def RegisterView(request):
    if request.user.is_authenticated:
        messages.warning(request, f"{request.user.full_name}, you are already logged in!")
        return redirect('index')

    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.full_name = form.cleaned_data.get("full_name")
            user.email = form.cleaned_data.get("email")
            user.set_password(form.cleaned_data.get("password1"))
            user.save()

            # Authenticate and log in the user
            user = authenticate(request, email=user.email, password=form.cleaned_data.get("password1"))
            if user:
                login(request, user)
                messages.success(request, f"Hey {user.full_name}, you are now logged in!")
                return redirect('index')
            else:
                messages.error(request, "Something went wrong with the login process. Please try again.")
        else:
            messages.error(request, "There was an error in the registration form. Please correct it.")
    else:
        form = UserRegisterForm()

    return render(request, 'auth/register.html', {'form': form})


def Loginview(request):
    if request.user.is_authenticated:
        messages.warning(request, f"{request.user.full_name}, you are already logged in!")
        return redirect('index')

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        if not email or not password:
            messages.error(request, "Both email and password are required!")
            return redirect('sign-in')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, "User with this email does not exist!")
            return redirect('sign-in')

        user_auth = authenticate(request, email=email, password=password)
        if user_auth is not None:
            login(request, user_auth)
            messages.success(request, f"Welcome back, {user_auth.full_name}!")
            next_url = request.GET.get("next", "index")  # Redirect to 'next' if specified, else 'index'
            return redirect(next_url)
        else:
            messages.error(request, "Invalid email or password!")
            return redirect('sign-in')

    return render(request, 'auth/sign-in.html')


def LogOutView(request):
    logout(request)
    messages.success(request,"You are log out!")
    return redirect('sign-in')
