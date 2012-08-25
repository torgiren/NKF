from django.contrib import admin
from NKF.core.models import *
models=(JM,VAT,Towar)
for mod in models:
	admin.site.register(mod)

