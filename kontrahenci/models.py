# -*- coding: utf-8 -*-
from django.db import models
from django.core.exceptions import ValidationError
def nip_validate(value):
	if len(value)!=10:
		raise ValidationError(u'Niepoprawna długość NIPu')
	suma=0
	suma+=int(value[0])*6
	suma+=int(value[1])*5
	suma+=int(value[2])*7
	suma+=int(value[3])*2
	suma+=int(value[4])*3
	suma+=int(value[5])*4
	suma+=int(value[6])*5
	suma+=int(value[7])*6
	suma+=int(value[8])*7
	if int(value[9])!=suma%11:
		raise ValidationError(u'Niepoprawny NIP')
class Miasto(models.Model):
	nazwa=models.CharField(max_length=16)
	def __unicode__(self):
		return self.nazwa
	class Meta:
		ordering=['nazwa']
class Kontrahent(models.Model):
	nazwa=models.CharField(max_length=255)
	adres=models.CharField(max_length=100)
	miasto=models.ForeignKey(Miasto)
	nip=models.CharField(max_length=10,validators=[nip_validate])
	def __unicode__(self):
		return u"%s, %s"%(self.nazwa,self.miasto)
	def fullName(self):
		return u"%s, %s, %s"%(self.nazwa, self.miasto, self.adres)

# Create your models here.
