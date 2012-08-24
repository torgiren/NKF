from django import forms
from magazynier.core import models
class TowarForm(forms.ModelForm):
	class Meta:
		model=models.Towar
