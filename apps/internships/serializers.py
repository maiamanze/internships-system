from rest_framework import serializers
from .models import Practica

class PracticaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Practica
        fields = "__all__"
        read_only_fields = ("estado",)