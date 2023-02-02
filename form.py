from unittest.util import _MAX_LENGTH
from django import forms

class Login_id(forms.Form):
    username = forms.CharField( label = "username",max_length=50)
    pwd = forms.CharField( label= "pwd", max_length=50)