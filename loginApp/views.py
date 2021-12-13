from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

def home(request):
    return render(request, "home.html", {}) 

def logged(request):
    if request.method == "POST":
        pass
    else:
        return render(request, "logged.html", {}) 

