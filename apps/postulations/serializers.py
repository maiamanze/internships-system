from rest_framework import serializers
from .models import Postulacion

class PostulacionListSerializer(serializers.ModelSerializer):
    estudiante = serializers.StringRelatedField()
    oferta = serializers.StringRelatedField()

    class Meta:
        model = Postulacion
        fields = (
            "id",
            "estudiante",
            "oferta",
            "estado",
            "fecha",
        )

class PostulacionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postulacion
        fields = ("oferta",)