from django.contrib import admin
from .models import Practica
from apps.tutors.models import Tutor
from django.core.exceptions import ValidationError

@admin.register(Practica)
class PracticaAdmin(admin.ModelAdmin):
    list_display = ("estudiante", "empresa", "estado", "fecha_inicio", "fecha_fin")
    list_filter = ("estado", "empresa")
    readonly_fields = ("estado",)
    actions = [
        "approve_academically",
        "activate",
    ]

    def approve_academically(self, request, queryset):
        for practica in queryset:
            try:
                practica.approve_academically(practica.tutor_academico)
            except ValidationError as e:
                self.message_user(request, str(e), level="error")
                return 
            
        self.message_user(request, "Prácticas aprobadas académicamente!")

    def activate(self, request, queryset):
        for practica in queryset:
            try:
                practica.activate()
            except ValidationError as e:
                self.message_user(request, str(e), level="error")
                return

        self.message_user(
            request,
            "Practices activated successfully."
        )

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "tutor_academico":
            kwargs["queryset"] = Tutor.objects.filter(tipo="ACADEMIC")

        if db_field.name == "tutor_empresarial":
            kwargs["queryset"] = Tutor.objects.filter(tipo="COMPANY")

        return super().formfield_for_foreignkey(db_field, request, **kwargs)