from django.contrib import admin
#importar modelo
from .models import Persona, Socio, Cajera, Oficial
# Register your models here.
admin.site.register(Persona)
admin.site.register(Socio)
admin.site.register(Cajera)
admin.site.register(Oficial)