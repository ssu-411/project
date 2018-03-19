from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.forms import CharField, PasswordInput

from .models import User, MyUser


class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class MyUserRegisterForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['gender', 'age']


class PasswordChangeCustomForm(PasswordChangeForm):
    error_css_class = 'has-error'
    error_messages = {'password_incorrect': "Неверный старый пароль. Повторите попытку."}
    old_password = CharField(required=True, label='Текущий пароль',
                             widget=PasswordInput(attrs={
                                 'class': 'form-control'}),
                             error_messages={
                                 'required': 'Пароль не может быть пустым'})

    new_password1 = CharField(required=True, label='Новый пароль',
                              widget=PasswordInput(attrs={
                                  'class': 'form-control'}),
                              error_messages={
                                  'required': 'Пароль не может быть пустым'})

    new_password2 = CharField(required=True, label='Новый пароль (подтверждение)',
                              widget=PasswordInput(attrs={
                                  'class': 'form-control'}),
                              error_messages={
                                  'required': 'Пароль не может быть пустым'})
