# Create your views here.
from django.shortcuts import render_to_response,redirect,get_object_or_404
from django.http import HttpResponse
from models import *
from NKF.core.models import *
from NKF.kontrahenci.models import *
def index(request):
	return render_to_response('ajax_index.html')
def ajax_towar(request,id):
	obj=get_object_or_404(Towar,id=id)
	ceny=dict()
	ceny['zakup_netto']=obj.zakup_netto();
	ceny['zakup_brutto']=obj.zakup_brutto()
	ceny['sprzedaz_netto']=obj.sprzedaz_netto()
	ceny['sprzedaz_brutto']=obj.sprzedaz_brutto()
	return render_to_response('ajax_towar.html',dict({'towar':obj}.items()+ceny.items()))
def ajax_kontrahent(request,id):
	obj=get_object_or_404(Kontrahent,id=id)
	return render_to_response('ajax_kontrahent.html',{'kontrahent':obj})	
def ajax_cena_zakupu_netto(request,id):
	obj=get_object_or_404(Towar,id=id)
	return HttpResponse(obj.zakup_netto())
def ajax_cena_sprzedazy_brutto(request,id):
	obj=get_object_or_404(Towar,id=id)
	return HttpResponse(obj.sprzedaz_brutto())
def ajax_menu_state(request,menu):
	if menu in request.session:
		del request.session[menu]
	else:
		request.session[menu]=True
	return HttpResponse("")
