# Create your views here.
from django.shortcuts import render_to_response,redirect,get_object_or_404
from models import *
from forms import *

def dodaj(request):
	kon=Kontrahent.objects.all()
	if request.method=='POST':
		form=FakturaForm(request.POST)
		if form.is_valid():
			id=form.save().id
			return redirect('/faktura/dodaj/%d'%id)
		else:
			return render_to_response('faktura_add.html',{'kontrahenci':kon,'blad':True})
	else:
		return render_to_response('faktura_add.html',{'kontrahenci':kon})
def dodaj_towary(request, id):
	faktura=get_object_or_404(Faktura,id=id)	

