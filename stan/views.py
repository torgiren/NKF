# Create your views here.
import NKF.core.models
import NKF.faktury.models
from datetime import *
from django.shortcuts import render_to_response, HttpResponse
def okres(request):
	if request.method=='POST' and request.POST['data']:
		return generuj(request.POST['data'])
	return render_to_response('okres.html',{'data':date.isoformat(date.today())})
def generuj(data):
	faktury=NKF.faktury.models.Faktura.objects.filter(data__lte=data)
	paragony=NKF.faktury.models.Paragon.objects.filter(data__lte=data)
	stan={}
	for fakt in faktury:
		zakupy=fakt.towary.all()
		for zak in zakupy:
			if zak.towar.nazwa not in stan:
				stan[str(zak.towar.nazwa)]=0
			stan[str(zak.towar.nazwa)]+=zak.ilosc
	for par in paragony:
		zakupy=par.towary.all()
		for zak in zakupy:
			if zak.towar.nazwa not in stan:
				stan[str(zak.towar.nazwa)]=0
			stan[str(zak.towar.nazwa)]-=zak.ilosc
	return render_to_response('stan.html',{'stan':stan})
