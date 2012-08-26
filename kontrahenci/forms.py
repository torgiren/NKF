from django import forms
from NKF.kontrahenci import models
class MiastoForm(forms.ModelForm):
	class Meta:
		model=models.Miasto
class KontrahentForm(forms.ModelForm):
	class Meta:
		model=models.Kontrahent

