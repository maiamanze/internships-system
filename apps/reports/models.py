from django.db import models
from apps.internships.models import Practica
from apps.tutors.models import Tutor
from django.utils import timezone

class Reporte(models.Model):
    REPORT_TYPE_CHOICES = [
        ("ROUTINE", "Rutinario"),
        ("FINAL", "Final"),
    ]

    practica = models.ForeignKey(Practica, on_delete=models.CASCADE, related_name="reports")
    tutor = models.ForeignKey(Tutor, on_delete=models.PROTECT, related_name="reports")
    tipo = models.CharField(max_length=20, choices=REPORT_TYPE_CHOICES, default="ROUTINE")
    fecha = models.DateField(default=timezone.now)
    documento = models.FileField(upload_to="reports/", null=True)
    observaciones = models.TextField(blank=True)
    aprobado = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Informe"
        verbose_name_plural = "Informes"

    def __str__(self):
        return f"Informe {self.get_tipo_display()} - {self.practica}"