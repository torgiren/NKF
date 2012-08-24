# Create your views here.
from django.shortcuts import render_to_response,redirect
from forms import *
def dodaj_towar(request):
	form=TowarForm()
	html=render_to_response('towary_add.html',dictionary={'form':form})
	return html
def dodaj_vat(request):
	if request.method=='POST':
		form=VATForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/manage');
	else:
		form=VATForm()
		html=render_to_response('vat_add.html',{'form':form})
		return html
