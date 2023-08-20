from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from django.core.exceptions import ValidationError
from .models import Profile
from django.contrib.auth.models import User

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileForm(forms.ModelForm):
    profile_pic = forms.ImageField(widget = forms.FileInput(attrs = {'class': 'file-form'}))
    class Meta:
        model=Profile

        fields = ['profile_pic', ]

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required = True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-field', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-field',
            'placeholder': 'Password',

        }
))
