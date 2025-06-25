from django.contrib import admin
from .models import Parroquia, Barrio

class ParroquiaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ubicacion', 'tipo')
    search_fields = ('nombre','tipo', 'ubicacion')
    list_filter = ('nombre', 'tipo', 'ubicacion')

class BarrioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'num_viviendas', 'num_parques', 'num_edificios', 'parroquia')
    search_fields = ('nombre', 'parroquia__nombre')
    list_filter = ('nombre', 'parroquia__tipo')

admin.site.register(Parroquia, ParroquiaAdmin)
admin.site.register(Barrio, BarrioAdmin)