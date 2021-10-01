from rest_framework import serializers
from .models import AdopcionModel, ProductoModel,DetalleModel,CabeceraModel




class AdopcionSerializer(serializers.ModelSerializer):
    class Meta:
        model=AdopcionModel

        fields='__all__'

        
class DetalleOperacionSerializer(serializers.Serializer):
    cantidad = serializers.IntegerField(required=True, min_value=1)

    importe = serializers.DecimalField(
        max_digits=5, decimal_places=2, min_value=0.01, required=True)

    producto = serializers.IntegerField(required=True, min_value=1)


class OperacionSerializer(serializers.Serializer):
    tipo = serializers.ChoiceField(
        choices=[('V', 'VENTA'), ('C', 'COMPRA')], required=True)

    cliente = serializers.CharField(required=True, min_length=8, max_length=11)

    detalle = DetalleOperacionSerializer(many=True)



class DetalleOperacionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleModel
        exclude = ['cabeceras']
        depth = 1


class OperacionModelSerializer(serializers.ModelSerializer):
    cabeceraDetalles = DetalleOperacionModelSerializer(
        many=True)

    class Meta:
        model = CabeceraModel
        fields = '__all__'
        depth = 1
