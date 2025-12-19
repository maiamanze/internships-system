from django.db import models
from django.utils import timezone
from apps.students.models import Estudiante
from apps.offers.models import Oferta

class Postulacion(models.Model):
    STATUS_CHOICES = [
        ("PENDING", "Pendiente"),
        ("ACCEPTED", "Aceptada"),
        ("REJECTED", "Rechazada"),
        ("WITHDRAWN", "Retirada")
    ]

    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name="postulations")
    oferta = models.ForeignKey(Oferta, on_delete=models.CASCADE, related_name="postulations")
    estado = models.CharField(max_length=20, choices=STATUS_CHOICES, default="PENDING")
    fecha = models.DateField(default=timezone.now)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["estudiante", "oferta"],
                name="unique_postulation_per_student_and_offer"
            )
        ]
        verbose_name = "Postulación"
        verbose_name_plural = "Postulaciones"

    def __str__(self):
        return f"{self.estudiante} → {self.oferta}"