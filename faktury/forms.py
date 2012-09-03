#-*- coding: utf-8 -*-
from django import forms
import models
from django.contrib.admin import widgets 
class FakturaForm(forms.ModelForm):
	class Meta:
		model=models.Faktura
class ZakupForm(forms.ModelForm):
	class Meta:
		model=models.Zakup
