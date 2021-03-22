from django.http import HttpResponse
from requests import Request, post
from django.shortcuts import render, redirect

def home(request):
    return render(request, 'spotify/home.html' )

def signIn(request):
    return render(request, 'spotify/signIn.html')

def logIn(request):
    return render(request, 'spotify/logIn.html')

def register(request):
    return render(request, 'spotify/register.html')

def dashboard(request):
    return render(request, 'spotify/dashboard.html')
