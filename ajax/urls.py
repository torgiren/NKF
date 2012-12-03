from django.conf.urls.defaults import patterns, include, url
import views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'magazynier.views.home', name='home'),
    # url(r'^magazynier/', include('magazynier.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
	url(r'^$',views.index),
	url(r'^towar/(?P<id>\d+)/$',views.ajax_towar),
	url(r'^towar/(?P<id>\d+)/cena_zakupu_netto/$',views.ajax_cena_zakupu_netto),
	url(r'^towar/(?P<id>\d+)/cena_sprzedazy_brutto/$',views.ajax_cena_sprzedazy_brutto),
	url(r'^kontrahent/(?P<id>\d+)/$',views.ajax_kontrahent),
	url(r'^menu/(?P<menu>\w+)/$',views.ajax_menu_state),
	
)
