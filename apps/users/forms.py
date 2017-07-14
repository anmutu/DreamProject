# _*_ coding:utf-8 _*_
__author__ = 'Ando'
__date__ = '7/14/2017 3:13 PM'

from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)