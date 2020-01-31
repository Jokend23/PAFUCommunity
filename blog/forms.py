from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django import forms

from .models import *


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'size': '40', 'class': 'form-control'}))
    sender = forms.EmailField(widget=forms.TextInput(attrs={'size': '40', 'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    copy = forms.BooleanField(required=False)

    class Meta:
        models = Contact
        field = ('subject', 'sender', 'message', 'copy')
