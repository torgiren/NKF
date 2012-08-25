from django.contrib import admin
from NKF.faktury.models import *
models=(Miasto,Kontrahent,Zakup,Faktura)
for mod in models:
	admin.site.register(mod)
