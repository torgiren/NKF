# Create your views here.
from django.shortcuts import render_to_response,redirect,get_object_or_404
from models import *
from forms import *
import forms
from datetime import *
from django.db import IntegrityError

def dodaj(request,what):
	if what.__name__=="Paragon":
		kon=None
		nr=paragon_next_number(date.today())
	else:
		nr=None
		kon=Kontrahent.objects.all()
	data=date.isoformat(date.today())
	if request.method=='POST':
		formFun=getattr(forms,"%sForm"%what.__name__)
#		formFun=locals()["%sForm"%what.__name__]
#		form=FakturaForm(request.POST)
		form=formFun(request.POST)
		if form.is_valid():
			id=form.save().id
			return redirect('/%s/%d/edit'%(what.__name__.lower(),id))
		else:
			return render_to_response('faktura_add.html',{'kontrahenci':kon,'blad':True,'what':what.__name__.lower(),'nr':nr,'data':data})
	else:
		return render_to_response('faktura_add.html',{'kontrahenci':kon,'what':what.__name__.lower(),'nr':nr,'data':data})
def dodaj_towary(request, id,what):
	url=request.path
	element=get_object_or_404(what,id=id)
	if request.method=='POST':
		form=ZakupForm(request.POST)	
		if form.is_valid():
			id=form.save()
			element.towary.add(id)
			obj=get_object_or_404(Towar,id=form.cleaned_data['towar'].id)
			old=obj.cena;
			new=form.cleaned_data['cena']
#			obj.cena=form.cleaned_data['cena']

			if old!=new:
				obj.cena=new
				obj.kalkulacja=True;
			obj.save()
			return redirect(url)
	dodane=element.towary.all()
	suma=0
	for i in dodane:
		suma+=i.wartosc()
	return render_to_response('towary_add.html',{'fakt':element,'url':url,'towary':Towar.objects.all(),'form':ZakupForm,'dodane':dodane,'suma':suma,'what':what.__name__.lower()})
from django.http import HttpResponse
def paragon_next_number(data):
	paragony=Paragon.objects.filter(data=data)
	lista=[]
	for par in paragony:
		lista.append(par.numer)
	if lista:
		return int(max(lista))+1
	else:
		return 1
