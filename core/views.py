# Create your views here.
from django.shortcuts import render_to_response
from forms import *
def dodaj_towar(request):
	form=TowarForm()
	html=render_to_response('towary_add.html',dictionary={'form':form})
	return html
