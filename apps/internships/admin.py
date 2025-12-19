from django.contrib import admin
from .models import Practica
from apps.tutors.models import Tutor

@admin.register(Practica)
class PracticaAdmin(admin.ModelAdmin):
    list_display = ("estudiante", "empresa", "estado", "fecha_inicio", "fecha_fin")
    list_filter = ("estado", "empresa")

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "tutor_academico":
            kwargs["queryset"] = Tutor.objects.filter(tipo="ACADEMIC")

        if db_field.name == "tutor_empresarial":
            kwargs["queryset"] = Tutor.objects.filter(tipo="COMPANY")

        return super().formfield_for_foreignkey(db_field, request, **kwargs)