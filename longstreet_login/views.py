from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django import forms

# Create your views here.

def home(request):
    return render(request, 'longstreet_login/home.html')

def register(request):
    if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
        User.objects.create_user(username, email, password)
        user = authenticate(username = username, password = password)
        login(request, user)
        return HttpResponseRedirect('/')
    else:
        raise forms.ValidationError('Looks like a username with that email or password already exists')
    return render(request, 'longstreet_login/register.html', {'form' : form})