# Create your views here.
from django.shortcuts import render_to_response,redirect,get_object_or_404
from forms import *
from models import *

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
def edit(request,id,what):
	object=get_object_or_404(globals()[what],id=id)
	Form=globals()["%sForm"%what]
	if request.method=='POST':
		form=Form(data=request.POST,instance=object)
		form.save()
		return redirect('/manage')
	else:
		form=Form(instance=object)
		return render_to_response('add.html',{'form':form,'action':'/%s/%s/edit/'%(what.lower(),id)})
def delete(request,id,what):
	object=get_object_or_404(globals()[what],id=id)
	if request.method=='POST':
		object.delete()
		return render_to_response('deleted.html')
	else:
		return render_to_response('delete.html',{'action':'/%s/%s/delete/'%(what.lower(),id),'item':object})
