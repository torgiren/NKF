#coding=utf8
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase

from models import *
from views import *

class VATTest(TestCase):
	@classmethod
	def setUpClass(self):
		pass		
class TowarTest(TestCase):
	@classmethod
	def setUpClass(self):
		self.towary=[]

		self.vat=VAT()
		self.vat.wartosc=7
		
		self.towar=Towar()
		self.towar.cena=12.40
		self.towar.vat=self.vat
		self.towar.marza=25.10
	
	def testNettoZakup(self):
		"""sprawdzam cene netto zakupu"""
		self.assertEqual(self.towar.zakup_netto(),12.40)
	def testNettoSprzedaz(self):
		u"""sprawdzam cene netto sprzedazy"""
		self.assertEqual(self.towar.sprzedaz_netto(),15.51)
	def testBruttoZakup(self):
		"""sprawdzam cene zakupu brutto"""
		self.assertEqual(self.towar.zakup_brutto(),13.27)
	def testBruttoSprzedaz(self):
		"""sprawdzam cene sprzedazy brutto"""
		self.assertEqual(self.towar.sprzedaz_brutto(),16.60)


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)
