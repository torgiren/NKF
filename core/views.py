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
			return render_to_response('add.html',{'form':form})
	else:
		form=VATForm()
		html=render_to_response('add.html',{'form':form,'action':'/vat/dodaj/'})
		return html
def list_vat(request):
	vats=VAT.objects.all()
	return render_to_response('list.html',{'items':vats,'type':'vat','suffix':'%'})
def edit_vat(request,id):
	object=get_object_or_404(VAT,id=id)
	if request.method=='POST':
		form=VATForm(data=request.POST,instance=object)
		form.save()
		return redirect('/manage')
	else:
		form=VATForm(instance=object)
		return render_to_response('add.html',{'form':form,'action':'/vat/%s/edit/'%id})
def delete_vat(request,id):
	object=get_object_or_404(VAT,id=id)
	if request.method=='POST':
		object.delete()
		return render_to_response('deleted.html')
	else:
		return render_to_response('delete.html',{'action':'/vat/%s/delete/'%id,'item':object})

def dodaj_jm(request):
	if request.method=='POST':
		form=JMForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/manage');
		else:
			return render_to_response('add.html',{'form':form})
	else:
		form=JMForm()
		html=render_to_response('add.html',{'form':form,'action':'/jm/dodaj/'})
		return html
def list_jm(request):
	jms=JM.objects.all()
	return render_to_response('list.html',{'items':jms,'type':'jm'})
def edit_jm(request,id):
	object=get_object_or_404(JM,id=id)
	if request.method=='POST':
		form=JMForm(data=request.POST,instance=object)
		form.save()
		return redirect('/manage')
	else:
		form=JMForm(instance=object)
		return render_to_response('add.html',{'form':form,'action':'/jm/%s/edit/'%id})
def delete_jm(request,id):
	object=get_object_or_404(JM,id=id)
	if request.method=='POST':
		object.delete()
		return render_to_response('deleted.html')
	else:
		return render_to_response('delete.html',{'action':'/jm/%s/delete/'%id,'item':object})



def dodaj_towar(request):
	if request.method=='POST':
		form=TowarForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/manage');
		else:
			return render_to_response('add.html',{'form':form})
	else:
		form=TowarForm()
		html=render_to_response('add.html',{'form':form,'action':'/towar/dodaj/'})
		return html
def list_towar(request):
	towars=Towar.objects.all()
	return render_to_response('list.html',{'items':towars,'type':'towar'})
def edit_towar(request,id):
	object=get_object_or_404(Towar,id=id)
	if request.method=='POST':
		form=TowarForm(data=request.POST,instance=object)
		form.save()
		return redirect('/manage')
	else:
		form=TowarForm(instance=object)
		return render_to_response('add.html',{'form':form,'action':'/towar/%s/edit/'%id})
def delete_towar(request,id):
	object=get_object_or_404(Towar,id=id)
	if request.method=='POST':
		object.delete()
		return render_to_response('deleted.html')
	else:
		return render_to_response('delete.html',{'action':'/towar/%s/delete/'%id,'item':object})
