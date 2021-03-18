from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework import status  # Used for anlaysis of return code
from rest_framework.views import APIView
import os
from requests import Request, post
from rest_framework.response import Response
from .forms import RegisterForm, LoginForm
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
client_id = os.environ.get('CLIENT_ID')
client_secret = os.environ.get('CLIENT_SECRET')
redirect_uri = os.environ.get('REDIRECT_URI')

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect("/")
    else:
        form = RegisterForm()

    return render(response, "register.html", {"form":form})

def authentication(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],
                        password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    #return HttpResponse('Authenticated ' \
                    #       'successfully')
                    return HttpResponseRedirect('/home/')
            else:
                return HttpResponse('Disabled account')

        else:
            return HttpResponse('Invalid login')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

def home(request):
    return render(request, 'spotify/home.html' )

class AuthURL(APIView):
    def get(self, request, fornat=None):
        scopes = 'user-read-playback-state user-modify-playback-state user-read-currently-playing'

        url = Request('GET', 'https://accounts.spotify.com/authorize', params={
            'scope': scopes,
            'response_type': 'code',
            'redirect_uri': redirect_uri,
            'client_id': client_id
        }).prepare().url
        return redirect(url)
        #return Response({'url': url}, status=status.HTTP_200_OK)

def spotify_callback(request, format=None):
    code = request.GET.get('code')
    error = request.GET.get('error')

    response = post('https://accounts.spotify.com/api/token', data={
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': redirect_uri,
        'client_id': client_id,
        'client_secret': client_secret
    }).json()

    access_token = response.get('access_token')
    token_type = response.get('token_type')
    refresh_token = response.get('refresh_token')
    expires_in = response.get('expires_in')
    error = response.get('error')

    if not request.session.exists(request.session.session_key):
        request.session.create()

    update_or_create_user_tokens(
        request.session.session_key, access_token, token_type, expires_in, refresh_token)

    return redirect('home:')

class IsAuthenticated(APIView):
    def get(self, request, format=None):
        is_authenticated = is_spotify_authenticated(
            self.request.session.session_key)
        return Response({'status': is_authenticated}, status=status.HTTP_200_OK)
