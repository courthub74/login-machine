from django.shortcuts import render

def home(request):
    return render(request, "home.html", {}) 

def logged(request):
    return render(request, "logged.html", {}) 

