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
def logout_user(request):
    logout(request)
    messages.success(request, ('You are logged out'))
    return redirect('home')

#SALESFORCE DEMO PAGE
def sfdemo(request):
    return render(request, "sfdemo.html", {})

#SALESFORCE LOGIN
def sflogin(request):
    if request.method == "POST":
        username2 = request.POST['username2'] #username2 is what is entered in the input area of name='username2'
        password2 = request.POST['password2'] #password2 is what is entered in the input area of name='password2'
        user = authenticate(request, username=username2, password=password2)
        if user is not None:
            login(request, user)
            messages.success(request, ('Login Success'))
            return redirect('sfdemo')
        else:
            messages.success(request, ('Error Logging In'))
            return redirect('home')
    else:
        return render(request, "home.html", {}) 