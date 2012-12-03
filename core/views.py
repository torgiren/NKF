# Create your views here.
from django.shortcuts import render_to_response,redirect,get_object_or_404
from django.http import HttpResponse
from django.template.context import RequestContext
from forms import *
from models import *

def dodaj(request,what,whatForm):
	request.session['proba']="Test2"
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
		html=render_to_response('add.html',{'form':form,'action':'/%s/dodaj/'%what.__name__.lower()},context_instance=RequestContext(request))
		request.session['return_page']=None
		return html
def list(request,what):
	request.session['proba']="Test"
#	items=globals()['%s'%what].objects.all()
	items=what.objects.all()
	dict={'items':items,'type':what.__name__.lower()}
	if what=='VAT':
		dict['suffix']='%'
	if what==Towar:
		class calc:
			action='kalkulacja'
			symbol='<img src="/media/calculator.png"/>'
			alt='Kalkulacja cen'
		tab=[calc,]
		dict['opts']=tab
	html= render_to_response('list.html',dict,context_instance=RequestContext(request))
	return html
def edit(request,id,what,whatForm,action_prefix=None,return_page=None):
	object=get_object_or_404(what,id=id)
	Form=whatForm
	if request.method=='POST':
		form=Form(data=request.POST,instance=object)
		form.save()
		if request.session['return_page']:
			return redirect(request.session['return_page'])
		else:
			return redirect('/manage')
	else:
		form=Form(instance=object)
#		request.session['return_page']=request.path
		request.session['return_page']=request.META['HTTP_REFERER']
		return render_to_response('add.html',{'form':form,'action':'/%s/%s/edit/'%(what.__name__.lower(),id),'action_prefix':action_prefix},context_instance=RequestContext(request))
def delete(request,id,what,action_prefix=None):
	object=get_object_or_404(what,id=id)
	if request.method=='POST':
		object.delete()
		if request.session['return_page']:
			return redirect(request.session['return_page'])
		else:
			return render_to_response('deleted.html',context_instance=RequestContext(request))
	else:
		if 'HTTP_REFERER' in request.META:
			request.session['return_page']=request.META['HTTP_REFERER']
		else:
			request.session['return_page']='/manage'
		return render_to_response('delete.html',{'action':'/%s/%s/delete/'%(what.__name__.lower(),id),'item':object,'action_prefix':action_prefix},context_instance=RequestContext(request))
def kalkulacja(request,id):
	if request.method=='POST' and request.POST['marza']:
		obj=get_object_or_404(Towar,id=id)
		obj.marza=request.POST['marza']
		obj.kalkulacja=False;
		obj.save()
		return redirect(request.session['return_page'])
	else:
		if 'HTTP_REFERER' in request.META:
			request.session['return_page']=request.META['HTTP_REFERER']
		else:
			request.session['return_page']='/manage'
		obj=get_object_or_404(Towar,id=id)
		return render_to_response('kalkulacja.html',{'towar':obj},context_instance=RequestContext(request))
