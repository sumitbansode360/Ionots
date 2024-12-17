from django import forms
from django.contrib.auth.forms import UserCreationForm
from userauths.models import User



class UserRegisterForm(UserCreationForm):
    full_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Enter full name", "class":"form-control"}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Enter username", "class":"form-control"}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':"Enter email address", "class":"form-control"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':"Enter password", "class":"form-control"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':"Confirm Password", "class":"form-control"}))

    class Meta:
        model = User
        fields = ["full_name", "username", "email", "password1", "password2"]