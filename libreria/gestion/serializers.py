from rest_framework import serializers
from .models import ProductoModel
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.conf import settings

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductoModel

        fields='__all__'

        # exclude= ['productoId']

class ImagenSerializer(serializers.Serializer):

    archivo = serializers.ImageField(
        max_length=20, use_url=True)

    def save(self):
        archivo: InMemoryUploadedFile = self.validated_data.get('archivo')
        print(archivo.content_type)
        print(archivo.name)
        print(archivo.size)
        ruta = default_storage.save(archivo.name, ContentFile(archivo.read()))
        return settings.MEDIA_URL + ruta   