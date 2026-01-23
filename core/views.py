from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'core/index.html')

def about(request):
    return render(request, 'core/about.html')

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("profile")
    else:
        form = RegisterForm()

    return render(request, "auth/register.html", {"form": form})




@login_required
def profile_view(request):
    user = request.user
    return render(request, "auth/profile.html", {"user": user})
