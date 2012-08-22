import os
import sys
path='/home/torgiren/python'
if path not in sys.path:
	sys.path.insert(0,path)
os.environ['DJANGO_SETTINGS_MODULE']='magazynier.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
