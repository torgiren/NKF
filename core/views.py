# Create your views here.
from django.shortcuts import render_to_response,redirect,get_object_or_404
from forms import *
from models import *
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





def dodaj(request,what):
	Form=globals()["%sForm"%what]
	if request.method=='POST':
		form=Form(request.POST)
#		form=TowarForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/manage');
		else:
			return render_to_response('add.html',{'form':form})
	else:
		form=Form()
		html=render_to_response('add.html',{'form':form,'action':'/%s/dodaj/'%what.lower()})
		return html
def list(request,what):
	items=globals()['%s'%what].objects.all()
	return render_to_response('list.html',{'items':items,'type':what.lower()})
