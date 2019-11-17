from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


# Create your views here.

def signup(request):
    if request.method == "POST":
        if request.POST["password"] == request.POST["password2"]:
            user = User.objects.create_user(
                username=request.POST["username"], password=request.POST["password"])
            auth.login(request, user)
            return render(request, 'accounts/signup_complete.html')
        return render(request, 'accounts/signup.html')

    return render(request, 'accounts/signup.html')

