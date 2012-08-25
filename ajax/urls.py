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
)
