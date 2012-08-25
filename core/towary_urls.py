from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
import views
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'magazynier.views.home', name='home'),
    # url(r'^magazynier/', include('magazynier.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
#	url(r'^$',include('magazynier.core.urls')),
	url(r'^$',views.list,{'what':'Towar'}),
	url(r'^dodaj/$',views.dodaj,{'what':'Towar'}),
	url(r'^(?P<id>\d+)/edit/$',views.edit,{'what':'Towar'}),
	url(r'^(?P<id>\d+)/delete/$',views.delete_towar),


)
