from django.conf.urls.defaults import patterns, include, url
import NKF.core.views
from models import *
import views
urlpatterns = patterns('',
	url(r'^$',views.okres),
)

