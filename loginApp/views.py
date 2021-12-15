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
def salesforce_login(request):
    if request.method == "POST":
        sfname = request.POST['sfname']
        sfpassword = request.POST['sfpassword']
        user = authenticate(request, sfname=sfname, sfpassword=sfpassword)
        if user is not None:
            login(request, user)
            return redirect('sfdemo')
        else:
            return redirect('home')
    else: #If nothing happens just go back to home page
        return render(request, "home.html", {})
