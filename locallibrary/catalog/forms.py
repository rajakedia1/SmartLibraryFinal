from django import forms
from .models import Book
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime
from django.views import generic

class ReviewBookForm(forms.Form, generic.DetailView):
	model = Book
	new_review = forms.CharField(help_text="Enter review for this book")
	def clean_review(self):
		data = self.cleaned_data['new_review']

		if len(data)==0:
			raise ValidationError(_('Write something before submit'))

		if len(data)>100:
			raise ValidationError(_('Please write in less than 100 words'))

		return data


