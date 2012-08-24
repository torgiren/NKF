# Create your views here.
from django.shortcuts import render_to_response,redirect,get_object_or_404
from forms import *
from models import *
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
			return render_to_response('vat_add.html',{'form':form})
	else:
		form=VATForm()
		html=render_to_response('vat_add.html',{'form':form,'action':'/vat/dodaj/'})
		return html
def list_vat(request):
	vats=VAT.objects.all()
	return render_to_response('vat.html',{'items':vats})
def edit_vat(request,id):
	object=get_object_or_404(VAT,id=id)
	if request.method=='POST':
		form=VATForm(data=request.POST,instance=object)
		form.save()
		return redirect('/manage')
	else:
		form=VATForm(instance=object)
		return render_to_response('vat_add.html',{'form':form,'action':'/vat/%s/edit/'%id})

