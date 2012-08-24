from django import forms
from core import models
class TowarForm(forms.ModelForm):
	class Meta:
		model=models.Towar
