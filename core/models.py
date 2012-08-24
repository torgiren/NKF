from django.db import models

# Create your models here.
class JM(models.Model):
	nazwa=models.CharField(max_length=10)
class VAT(models.Model):
	wartosc=models.DecimalField(max_digits=3,decimal_places=0)
	def __unicode__(self):
		return u"%d"%self.wartosc
class Towar(models.Model):
	nazwa = models.CharField(max_length=30)
	jm=models.ForeignKey(JM)
#cena zakupu netto
	cena=models.DecimalField(max_digits=10,decimal_places=2)
	vat=models.ForeignKey(VAT)
	marza=models.DecimalField(max_digits=5,decimal_places=2)


