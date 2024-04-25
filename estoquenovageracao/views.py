from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.contrib import messages


# Create your views here.
def login_view(request):
    return render(request, 'login.html')


def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('admin/')
        else:
            messages.error(request, 'User or password is incorrect')
    return redirect('errado/')


def logout_view(request):
    logout(request)
