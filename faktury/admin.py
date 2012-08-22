from django.contrib import admin
from magazynier.faktury.models import *
models=(Miasto,Kontrahent,Zakup,Faktura)
for mod in models:
	admin.site.register(mod)
