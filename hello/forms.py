# coding=utf-8
from django import forms
from captcha.fields import ReCaptchaField

class ContactForm(forms.Form):
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class' : 'form-control'}))
    subject = forms.CharField(label="Subject", max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    message = forms.CharField(label="Message", widget=forms.Textarea(attrs={'class': 'form-control'}))
    captcha = ReCaptchaField(attrs={'class' : 'form-control'})
