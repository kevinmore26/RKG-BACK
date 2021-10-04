from rest_framework import serializers
from .models import AdopcionModel, ProductoModel,DetalleModel,CabeceraModel,ClienteModel
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings




class RegistroSerializer( serializers.ModelSerializer):
    def save(self):
        clienteNombre =self.validated_data.get('clienteNombre')
        clienteDocumento = self.validated_data.get('clienteDocumento')
        clienteCelular = self.validated_data.get('clienteCelular')
        clienteCorreo = self.validated_data.get('clienteCorreo')
        clientePassword = self.validated_data.get('clientePassword')
        perfilCliente =self.validated_data.get('perfilCliente')
        nuevoCliente = ClienteModel(clienteNombre=clienteNombre,clienteDocumento= clienteDocumento,clienteCelular=clienteCelular, clienteCorreo= clienteCorreo,clientePassword=clientePassword,perfilCliente=perfilCliente)
        nuevoCliente.set_password(clientePassword)
        nuevoCliente.save()
        return nuevoCliente
    
    class Meta:
        model = ClienteModel
        exclude = ['groups','user_permissions','is_superuser','last_login']
        extra_kwargs= {
            'password':{
                'write_only': True,    
            }
        }

class AdopcionSerializer(serializers.ModelSerializer):
    adopcionFoto=serializers.CharField(max_length=100)
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


class ImagenSerializer(serializers.Serializer):
    archivo = serializers.ImageField(
        max_length=50, use_url=True)

    def save(self):
        archivo: InMemoryUploadedFile = self.validated_data.get('archivo')

        print(archivo.content_type)
        print(archivo.name)
        print(archivo.size)

        ruta = default_storage.save(archivo.name, ContentFile(archivo.read()))
        return settings.MEDIA_URL + ruta

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductoModel

        fields='__all__'