from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
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
	url(r'^$',direct_to_template,{'template':'base.html'}),
	url(r'^contact/$',direct_to_template,{'template':'contact.html'}),
	url(r'^features/$',direct_to_template,{'template':'features.html'}),
	url(r'^manage/$',direct_to_template,{'template':'manage.html'}),
	url(r'^towar/',include('NKF.core.towary_urls')),
	url(r'^vat/',include('NKF.core.vat_urls')),
	url(r'^jm/',include('NKF.core.jm_urls')),


    url(r'^admin/', include(admin.site.urls)),
	url(r'^media/(?P<path>.*)', 'django.views.static.serve',{'document_root': '/home/torgiren/python/NKF/media'}),
)
