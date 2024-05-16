from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
# from .forms import OrderForm, CreateUserForm
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate
# Create your views here.
def home(request):
    context = {}
    return render(request, 'home.html', context)

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')
    context  = {'form': form}
    return render(request, 'register.html', context)


def login(request):
    form = LoginForm()
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse('Invalid login')
    context = {'form': form}
    return render(request, 'login.html', context)