from django.http import HttpResponse
from requests import Request, post
from django.shortcuts import render, redirect

def home(request):
    return render(request, 'spotify/signIn.html' )
