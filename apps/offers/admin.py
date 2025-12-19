from django.contrib import admin
from .models import Oferta

@admin.register(Oferta)
class OfferAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'empresa', 'estado', 'duracion_meses', 'horas_semanales', 'remuneracion')
    list_filter = ('estado', 'empresa')
    search_fields = ('titulo', 'empresa__nombre')

# Register your models here.
