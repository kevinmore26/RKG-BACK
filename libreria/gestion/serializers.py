from rest_framework import serializers
from .models import ProductoModel,DetalleModel,CabeceraModel

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

    # detalle2= serializers.ListField(child=DetalleOperacionSerializer)


class DetalleOperacionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleModel
        # fields = '__all__'
        exclude = ['cabeceras']
        depth = 1


class OperacionModelSerializer(serializers.ModelSerializer):
    cabeceraDetalles = DetalleOperacionModelSerializer(
        # source='cabeceraDetalles',
        many=True)

    class Meta:
        model = CabeceraModel
        fields = '__all__'
        # con el atributo depth indicare cuantos niveles quiero agregar para mostrar la informacion en el caso de las FK's
        depth = 1
