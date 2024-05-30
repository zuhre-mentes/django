from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User



class LoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

class UserRegistrationForm(forms.ModelForm):

    username = forms.CharField(label="Username", max_length=100, widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control', 'placeholder': 'Username'}))
    email = forms.EmailField(label="E-mail", max_length=100, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-mail'}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

