"""music_controller URL Configuration

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
from django.urls import path, include
from spotify import views as v
from spotify import backends as b
from spotify.userModels import Account as a
from frontend.views import home, signIn, dashboard, settings

urlpatterns = [
    path('', v.home),
    path('home/', v.home),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', include('frontend.urls')),
    path('spotify/', include('spotify.urls')),
    path("logIn", v.logIn, name="logIn"),
    path("logOut", v.logOut, name="logOut"),
    path("register/", v.register, name="register"),
    path('signIn', signIn),
    path("dashboard.html", dashboard),
    path('setGender', a.set_gender, name='setGender'),
    path('setEmail', a.set_email, name='setEmail'),
    path('setUsername', a.set_username, name='setUserName'),
    path('setPassword', a.set_password, name='setPassword'),
    path('setFirstName', a.set_first_name, name='setFirstName'),
    path('setLastName', a.set_last_name, name='setLastName'),
    path('setPhone', a.set_phone, name='setPhone'),
    path('setInsta', a.set_insta, name='setInsta'),
    path('setLocation', a.set_location, name='setLocation'),
    path('setLowAge', a.set_low_age, name='setLowAge'),
    path('setHighAge', a.set_high_age, name='setHighAge'),
    path('setBio', a.set_bio, name='setBio'),
    path('setGenderPref', a.set_gender_preference, name='setGenderPref'),
]
