from django.conf.urls.defaults import patterns, include, url
import NKF.core.views
from models import *
from forms import *
import views
urlpatterns = patterns('',
	url(r'^$',NKF.core.views.list),
	url(r'^dodaj/$',views.dodaj),
	url(r'^(?P<id>\d+)/edit/$',views.dodaj_towary),
#	url(r'^(?P<id>\d+)/edit/$',NKF.core.views.edit,{'what':Faktura,'whatForm':FakturaForm}),
	url(r'^(?P<id>\d+)/delete/$',NKF.core.views.delete),
	url(r'^\d+/zakup/$',NKF.core.views.dodaj,{'what':Zakup,'whatForm':ZakupForm,'action_prefix':'faktura'}),
	url(r'^zakup/(?P<id>\d+)/edit/$',NKF.core.views.edit,{'what':Zakup,'whatForm':ZakupForm,'action_prefix':'faktura'}),
	url(r'^zakup/(?P<id>\d+)/delete/$',NKF.core.views.delete,{'what':Zakup,'action_prefix':'faktura'}),

)
