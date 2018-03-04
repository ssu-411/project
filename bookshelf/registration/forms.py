from django import forms
from .models import User, MyUser


class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class MyUserRegisterForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['gender', 'age']
