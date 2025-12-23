from django.db import models
from django.utils import timezone
from apps.students.models import Estudiante
from apps.offers.models import Oferta
from apps.internships.models import Practica
from django.core.exceptions import ValidationError

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

    def accept(self, accepted_by_user):
        if self.estado != "PENDING":
            raise ValidationError("La postulación no está pendiente")
        
        if self.oferta.estado == "CLOSED":
            raise ValidationError("La oferta cerró.")
        
        # Permiso: Empresa creadora de la oferta o tutor empresarial de esa empresa
        company = self.oferta.empresa
        is_offer_creator = accepted_by_user == company.usuario
        is_company_tutor = (
            hasattr(accepted_by_user, "tutor")
            and accepted_by_user.tutor.tipo == "COMPANY"
            and accepted_by_user.tutor.empresa == company
        )

        if not (is_offer_creator or is_company_tutor):
            raise ValidationError("Sólo la empresa o su tutor pueden aceptar una postulación")
        
        if Practica.objects.filter(oferta=self.oferta).exists():
            raise ValidationError("Esta oferta ya tiene una práctica asociada.")
        
        # Aceptar postulación
        self.estado = "ACCEPTED"
        self.save()

        # Rechazar las demás
        Postulacion.objects.filter(
            oferta=self.oferta
        ).exclude(pk=self.pk).update(estado="REJECTED")

        # Crear práctica
        Practica.objects.create(
            estudiante=self.estudiante,
            empresa=self.oferta.empresa,
            oferta=self.oferta,
            estado="PENDING"
        )

        # Cerrar oferta
        self.oferta.close()

    def __str__(self):
        return f"{self.estudiante} → {self.oferta}"