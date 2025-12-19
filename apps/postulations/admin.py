from django.contrib import admin
from .models import Postulacion

@admin.register(Postulacion)
class PostulationAdmin(admin.ModelAdmin):
    list_display = ('estudiante', 'oferta', 'estado', 'fecha')
    list_filter = ('estado', 'fecha')
    search_fields = ('estudiante__usuario__first_name',
                    'estudiante__usuario__last_name',
                    'estudiante__dni',
                    'oferta__titulo',
                    'oferta__empresa__nombre')
