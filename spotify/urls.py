from django.urls import path
from .views import AuthURL, spotify_callback, IsAuthenticated, logIn

urlpatterns = [
    path('get-auth-url', AuthURL.as_view(), name="get-auth-url"),
    path('redirect', spotify_callback),
    path("logIn", logIn, name="logIn"),
    path('is-authenticated', IsAuthenticated.as_view())
]
