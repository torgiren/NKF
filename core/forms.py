from django import forms
from NKF.core import models
class TowarForm(forms.ModelForm):
	class Meta:
		model=models.Towar
class VATForm(forms.ModelForm):
	class Meta:
		model=models.VAT
class JMForm(forms.ModelForm):
	class Meta:
		model=models.JM
