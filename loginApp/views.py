from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout

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
            return redirect('logged')
        else:
            return redirect('home')
    else:
        return render(request, "logged.html", {}) 

