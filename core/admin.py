from django.contrib import admin
from magazynier.core.models import *
models=(JM,VAT,Towar)
for mod in models:
	admin.site.register(mod)

