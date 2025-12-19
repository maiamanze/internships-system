from django.db import models
from django.contrib.auth.models import User

class Estudiante(models.Model):
    ACADEMIC_STATUS_CHOICES = [
        ("REGULAR", "Regular"),
        ("CONDICIONAL", "Condicional"),
        ("LIBRE", "Libre"),
        ("GRADUADO", "Graduado")
    ]

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    dni = models.CharField(max_length=20, unique=True)
    carrera = models.CharField(max_length=100)
    anio = models.PositiveIntegerField()
    estado_academico = models.CharField(max_length=20, choices=ACADEMIC_STATUS_CHOICES, default="REGULAR")
    
    def __str__(self):
        return f"{self.usuario.get_full_name()} ({self.dni})"
