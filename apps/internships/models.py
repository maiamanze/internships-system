from django.db import models
from apps.students.models import Estudiante
from apps.companies.models import Empresa
from apps.offers.models import Oferta
from apps.tutors.models import Tutor
from django.core.exceptions import ValidationError

class Practica(models.Model):
    STATUS_CHOICE = [
        ("ACTIVE", "Activa"),
        ("SUSPENDED", "Suspendida"),
        ("FINISHED", "Finalizada"),
        ("CANCELLED", "Cancelada")
    ]

    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name="practicas")
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name="practicas")
    tutor_academico = models.ForeignKey(Tutor, on_delete=models.PROTECT, related_name="academic_practices", null=True, blank=True)
    tutor_empresarial = models.ForeignKey(Tutor, on_delete=models.PROTECT, related_name="company_practices", null=True, blank=True)
    oferta = models.OneToOneField(Oferta, on_delete=models.CASCADE) # Una oferta solo puede generar una práctica
    estado = models.CharField(max_length=20, choices=STATUS_CHOICE, default="ACTIVE")
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_fin = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = "Práctica"
        verbose_name_plural = "Prácticas"

    def save(self, *args, **kwargs):
        if self.estado == "ACTIVE":
            existing_active = Practica.objects.filter(estudiante=self.estudiante, estado="ACTIVE")

            if self.pk:
                existing_active = existing_active.exclude(pk=self.pk)

            if existing_active.exists():
                raise ValidationError("El estudiante ya tiene una práctica activa.")
            
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.estudiante} - {self.empresa}"