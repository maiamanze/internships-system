from django.db import models
from django.contrib.auth.models import User

class Tutor(models.Model):
    TUTOR_TYPE_CHOICES = [
        ("ACADEMIC", "Académico"),
        ("COMPANY", "Empresarial")
    ]

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=20, choices=TUTOR_TYPE_CHOICES)
    institucion = models.CharField(max_length=150, blank=True)

    class Meta:
        verbose_name = "Tutor"
        verbose_name_plural = "Tutores"

    def __str__(self):
        return f"{self.usuario.get_full_name()} ({self.get_tipo_display()})"