# Create your views here.
from django.shortcuts import render_to_response,redirect,get_object_or_404
from models import *
from forms import *
from django.db import IntegrityError

def dodaj(request):
	kon=Kontrahent.objects.all()
	if request.method=='POST':
		form=FakturaForm(request.POST)
		if form.is_valid():
			id=form.save().id
			return redirect('/faktura/%d/edit'%id)
		else:
			return render_to_response('faktura_add.html',{'kontrahenci':kon,'blad':True})
	else:
		return render_to_response('faktura_add.html',{'kontrahenci':kon})
def dodaj_towary(request, id):
	url=request.path
	faktura=get_object_or_404(Faktura,id=id)
	if request.method=='POST':
		form=ZakupForm(request.POST)	
		if form.is_valid():
			id=form.save()
			faktura.towary.add(id)
			obj=get_object_or_404(Towar,id=form.cleaned_data['towar'].id)
			old=obj.cena;
			new=form.cleaned_data['cena']
#			obj.cena=form.cleaned_data['cena']

			if old!=new:
				obj.cena=new
				obj.kalkulacja=True;
			obj.save()
			return redirect(url)
	dodane=faktura.towary.all()
	suma=0
	for i in dodane:
		suma+=i.wartosc()
	return render_to_response('towary_add.html',{'fakt':faktura,'url':url,'towary':Towar.objects.all(),'form':ZakupForm,'dodane':dodane,'suma':suma})
