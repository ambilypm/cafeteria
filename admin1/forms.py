from django import forms

class items(forms.Form):
    logo=forms.ImageField()
    name=forms.CharField(max_length=100)
    price=forms.IntegerField()

class Reg(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())