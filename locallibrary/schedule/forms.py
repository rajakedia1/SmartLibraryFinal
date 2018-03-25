from django import forms
from .models import Branch

class InfoForm(forms.Form):
	info = forms.CharField(max_length=1000)
	branch = forms.CharField(max_length=100)
	
