# -*- coding: utf-8 -*-
from django.db import models
#from magazynier.core.models import Towar
from NKF.core.models import *
from NKF.kontrahenci.models import *
# Create your models here.
class Zakup(models.Model):
	towar=models.ForeignKey(Towar,related_name='towar')
	ilosc=models.DecimalField(max_digits=5,decimal_places=3)
	cena=models.DecimalField(max_digits=10,decimal_places=2)
class Faktura(models.Model):
	kontrahent=models.ForeignKey(Kontrahent)
	data=models.DateField()
	towary=models.ForeignKey(Zakup)
