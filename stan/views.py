# Create your views here.
import NKF.core.models
import NKF.faktury.models
from django.shortcuts import render_to_response, HttpResponse
def ogolny(request):
	faktury=NKF.faktury.models.Faktura.objects.all()
	paragony=NKF.faktury.models.Paragon.objects.all()
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
