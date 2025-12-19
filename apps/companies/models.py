from django.db import models
from django.contrib.auth.models import User

class Empresa(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=150)
    cuit = models.PositiveBigIntegerField(unique=True)
    contacto = models.EmailField()
    rubro = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

