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
	def __unicode__(self):
		return u"%s, %.2f %s * %.2f zł + %.2f%% , %.2f zł"%(self.towar.nazwa,self.ilosc,self.towar.jm,self.cena,self.towar.vat.wartosc,self.wartosc())
	def cena_brutto(self):
		return round(self.cena*(1+self.towar.vat.wartosc/100),2)
	def wartosc(self):
		#TODO Z niewiadomych przyczyn nie dało się self.cena_brutto()*selt.ilosc
		return round(self.ilosc*self.cena*(1+self.towar.vat.wartosc/100),2)
	def sprzedaz_brutto(self):
		return round(self.towar.sprzedaz_brutto(),2)
	def wartosc_sprzedaz_brutto(self):
		return round(self.sprzedaz_brutto()*float(self.ilosc),2)
class DokumentSprzedazy(models.Model):
	data=models.DateField()
	towary=models.ManyToManyField(Zakup,blank=True,null=True)
	numer=models.CharField(max_length=30)
	def __unicode__(self):
		return u"%s, %s"%(self.numer,self.data)
	class Meta:
		abstract = True
class Paragon(DokumentSprzedazy):
	pass
class Faktura(DokumentSprzedazy):
	kontrahent=models.ForeignKey(Kontrahent)
#	data=models.DateField()
#	towary=models.ManyToManyField(Zakup,blank=True,null=True)
	def __unicode__(self):
		return u"%s, %s"%(self.kontrahent.nazwa,self.data)
