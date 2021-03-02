from django.urls import path
from spotify import views


urlpatterns = [
    path("", views.home, name="home"),
]
