"""
web_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from spotify import views as v
from spotify import backends as b
from .views import home, signIn, dashboard

urlpatterns = [
    path('', v.home),
    path('home/', v.home),
    path('admin/', admin.site.urls),
    path('spotify/', include('spotify.urls')),
    path("logIn", v.logIn, name="logIn"),
    path("logOut", v.logOut, name="logOut"),
    path("register/", v.register, name="register"),
    path('signIn', signIn),
    path("dashboard.html", dashboard)
]

