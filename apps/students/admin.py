from django.contrib import admin
from .models import Estudiante

@admin.register(Estudiante)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'dni', 'carrera', 'anio', 'estado_academico')
    search_fields = ('dni', 'user__first_name', 'user__last_name')

