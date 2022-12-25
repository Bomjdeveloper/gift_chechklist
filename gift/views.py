from django.shortcuts import render, redirect
from .models import Gift
from .forms import Create_gift
from django.contrib.auth import login as lg, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpResponse
from django.contrib.auth.models import User

def index(request): 
    if request.user.is_authenticated:
        name = Gift.objects.filter(user=request.user)
        return render(request, '../templates/home/index.html', {'name': name})
    else:
        return redirect('/registration')

def registration(request):
    if request.user.is_authenticated:
        return redirect('/home')
    else:
        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()

                lg(request, user)
                return redirect('/home')
            else:
                form = UserCreationForm()
    form = UserCreationForm()
    return render(request, '../templates/registration/registration.html', {'form': form})

def login(request):
    if request.user.is_authenticated:
        return redirect('/home')
    else:
        if request.method == "POST": 
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                user = form.get_user()
                lg(request, user)
                return redirect('/home')
            else:
                HttpResponse("Something went wrong")
                form = AuthenticationForm()
    form = AuthenticationForm()
    return render(request, '../templates/login/login.html', {'form': form})
        

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/registration')

def create(request):
    if request.user.is_authenticated:
        if request.method == "POST": 
            form = Create_gift(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.user = request.user
                form.save()
                return redirect('/home')
            else:
                HttpResponse("Something went wrong")
                form = Create_gift()
        form = Create_gift()
        return render(request, '../templates/create/new_gift.html', {'form': form})
    else:
        return redirect('/home')
def red(request):
    return redirect('/home')
    