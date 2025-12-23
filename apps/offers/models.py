from django.db import models
from apps.companies.models import Empresa
from django.utils import timezone

class Oferta(models.Model):
    STATUS_CHOICES = [
        ("OPEN", "Abierta"),
        ("CLOSED", "Cerrada")
    ]

    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name="offers")
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField()
    duracion_meses = models.PositiveIntegerField()
    horas_semanales = models.PositiveIntegerField()
    estado = models.CharField(max_length=20, choices=STATUS_CHOICES, default="OPEN")
    fecha_publicacion = models.DateField(null=True, blank=True)
    remuneracion = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.estado == "OPEN" and self.fecha_publicacion is None:
            self.fecha_publicacion = timezone.now().date()
        super().save(*args, **kwargs)

    def close(self):
        if self.estado == "CLOSED":
            return
        
        self.estado = "CLOSED"
        self.save()

    def __str__(self):
        return f"{self.titulo} - {self.empresa.nombre}"