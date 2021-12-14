from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

#HOME
def home(request):
    return render(request, "home.html", {}) 

#LOGIN
def logged(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('Login Success'))
            return redirect('logged')
        else:
            messages.success(request, ('Error Logging In'))
            return redirect('home')
    else:
        return render(request, "logged.html", {}) 

#LOGOUT
def logout(request):
    logout(request)
    messages.success(request, ('You are logged out'))
    return redirect('home')

