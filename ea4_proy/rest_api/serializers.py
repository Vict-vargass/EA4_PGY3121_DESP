from rest_framework import serializers
from core_app.models import Obra


class ObraSerializer(serializers.ModelSerializer):
    class Meta:
        model= Obra
        fields = ['nombreObra','historia','descripcion','precio','tecnicaUsada','categoria','imagen']