from django.contrib import admin
from .models import Museo, GuiaMuseo, Exhibicion

# Register your models here.

'''

Al momento de presentar la información de museos, se debe presentar, además, el costo total de producción en función de los costos de las exhibiciones y el nombre (es) del guía con más experiencia

'''


class ExhibicionInline(admin.ModelAdmin):
    list_display = ('titulo_exhibicion', 'duracion_meses', 'costo_produccion', 'tematica', 'guia_museo')

class MuseoInline(admin.ModelAdmin):
    list_display = ('nombre', 'ciudad', 'anio_fundacion', 'calcular_costo_total_produccion', 'guia_museo')
    
class GuiaMuseoInline(admin.ModelAdmin):
    list_display = ('nombre_completo', 'anios_experiencia_guia', 'idiomas_hablados', 'museo')


admin.site.register(Museo, MuseoInline)
admin.site.register(GuiaMuseo, GuiaMuseoInline)
admin.site.register(Exhibicion, ExhibicionInline)