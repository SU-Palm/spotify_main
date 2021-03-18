from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from spotify.userModels import Account


class RegisterForm(UserCreationForm):
    # email = forms.EmailField()

    class Meta:
        model = Account
        fields = ["email", "username", "password1"]

class LoginForm(AuthenticationForm):
    # email = forms.EmailField()

    class Meta:
        model = User
        fields = ["email", "password"]