from rest_framework import serializers
from .models import Autor, Libro

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = (
                    "id",
                    "nombre"
                )

class LibroSerializer(serializers.ModelSerializer):
    # autor = AutorSerializer()

    class Meta:
        model = Libro
        fields = (
                    "id",
                    "titulo",
                    "año_publicacion",
                    "precio",
                    "imagen",
                    "descripcion",
                    "stock",
                    "firmado",
                    "hay_envio_gratis",
                    "autor",
                )

