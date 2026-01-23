from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=False, label="Email", widget=forms.EmailInput(attrs={
        "placeholder": "Enter your email"
    }))

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        labels = {
            "username": "Username",
            "password1": "Password",
            "password2": "Confirm Password",
        }
        widgets = {
            "username": forms.TextInput(attrs={"placeholder": "Enter username"}),
            "password1": forms.PasswordInput(attrs={"placeholder": "Enter password"}),
            "password2": forms.PasswordInput(attrs={"placeholder": "Confirm password"}),
        }

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", widget=forms.TextInput(attrs={
        "placeholder": "Enter username"
    }))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={
        "placeholder": "Enter password"
    }))
