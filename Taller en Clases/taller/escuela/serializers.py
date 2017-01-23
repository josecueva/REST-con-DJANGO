from django.forms import widgets
from rest_framework import serializers
from escuela.models import Estudiante, LANGUAGE_CHOICES, STYLE_CHOICES

class EstudiantesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante 
        fields = ('id', 'nombre', 'apellido', 'cedula', 'ciudad', 'provincia')
