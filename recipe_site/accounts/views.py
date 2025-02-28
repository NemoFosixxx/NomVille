from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import *

def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = CustomUserCreationForm()
    
    return render(request, "accounts/register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("index")
    return render(request, "accounts/login.html")

def logout_view(request):
    logout(request)
    return redirect("index")
