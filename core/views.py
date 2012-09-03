# Create your views here.
from django.shortcuts import render_to_response,redirect,get_object_or_404
from forms import *
from models import *

def dodaj(request,what,whatForm):
	Form=whatForm
	if request.method=='POST':
		form=Form(request.POST)
#		form=TowarForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/%s/'%what.__name__.lower())
		else:
			return render_to_response('add.html',{'form':form})
	else:
		form=Form()
		html=render_to_response('add.html',{'form':form,'action':'/%s/dodaj/'%what.__name__.lower()})
		request.session['return_page']=None
		return html
def list(request,what):
#	items=globals()['%s'%what].objects.all()
	items=what.objects.all()
	dict={'items':items,'type':what.__name__.lower()}
	if what=='VAT':
		dict['suffix']='%'
	return render_to_response('list.html',dict)
def edit(request,id,what,whatForm):
	object=get_object_or_404(what,id=id)
	Form=whatForm
	if request.method=='POST':
		form=Form(data=request.POST,instance=object)
		form.save()
		return redirect('/manage')
	else:
		form=Form(instance=object)
		return render_to_response('add.html',{'form':form,'action':'/%s/%s/edit/'%(what.__name__.lower(),id)})
def delete(request,id,what):
	object=get_object_or_404(what,id=id)
	if request.method=='POST':
		object.delete()
		return render_to_response('deleted.html')
	else:
		return render_to_response('delete.html',{'action':'/%s/%s/delete/'%(what.__name__.lower(),id),'item':object})
