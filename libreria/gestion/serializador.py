from django.core.files.base import ContentFile
from rest_framework import serializers
from rest_framework.fields import ImageField
from .models import ClienteModel, PlatoModel, UsuarioModel
from django.core.files.storage import default_storage
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.conf import settings

class RegistroSerializer( serializers.ModelSerializer):
    def save(self):
        clienteNombre =self.validated_data.get('clienteNombre')
        clienteApellido = self.validated_data.get('clienteApellido')
        clienteDocumento = self.validated_data.get('clienteDocumento')
        clienteCelular = self.validated_data.get('clienteCelular')
        clienteCorreo = self.validated_data.get('clienteCorreo')
        password = self.validated_data.get('password')
        clienteTipo = self.validated_data.get('clienteTipo')
        nuevoCliente = ClienteModel(
            clienteNombre = clienteNombre,
            clienteApellido = clienteApellido,
            clienteDocumento = clienteDocumento,
            clienteCelular = clienteCelular,
            clienteCorreo = clienteCorreo,
            clienteTipo = clienteTipo
        )
        
        nuevoCliente. make_password(password)
        nuevoCliente.set_password(password)
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


