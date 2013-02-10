from django import forms
from NKF.core import models
class TowarForm(forms.ModelForm):
	class Meta:
		model=models.Towar
		exclude=('kalkulacja')
		initial={'cena':0,
				'marza':0}
class VATForm(forms.ModelForm):
	class Meta:
		model=models.VAT
class JMForm(forms.ModelForm):
	class Meta:
		model=models.JM
