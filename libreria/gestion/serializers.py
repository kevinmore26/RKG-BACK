from rest_framework import serializers
from .models import ProductoModel

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductoModel

        fields='__all__'

        # exclude= ['productoId']