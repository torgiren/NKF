# Create your views here.
from django.shortcuts import render_to_response,redirect,get_object_or_404
from models import *
from NKF.core.models import *
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
