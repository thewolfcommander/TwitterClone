from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=20, required=True, help_text = None, widget=forms.TextInput(attrs={'placeholder': 'Enter your username'}))
    email = forms.CharField(max_length=254, required=True, help_text = None, widget=forms.EmailInput(attrs={'placeholder': 'Enter your Email Address'}))
    password1 = forms.CharField(max_length=20, required=True, help_text=None, widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'}))
    password2 = forms.CharField(max_length=20, required=True, help_text=None, widget=forms.PasswordInput(attrs={'placeholder': 'Repeat Password'}))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')