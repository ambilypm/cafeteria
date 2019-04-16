from django import forms

class Reg(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())