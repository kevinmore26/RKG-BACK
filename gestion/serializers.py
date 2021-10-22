from rest_framework import serializers
from .models import AdopcionModel, DetallePedidoModel,PedidoModel, ProductoModel, clienteModel
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer




class RegistroSerializer( serializers.ModelSerializer):
    def save(self):
        clienteNombre =self.validated_data.get('clienteNombre')
        clienteApellido = self.validated_data.get('clienteApellido')
        clienteDocumento = self.validated_data.get('clienteDocumento')
        clienteCelular = self.validated_data.get('clienteCelular')
        clienteCorreo = self.validated_data.get('clienteCorreo')
        clientePassword = self.validated_data.get('password')
        clienteTipo = self.validated_data.get('clienteTipo')

        perfilCliente =self.validated_data.get('perfilCliente')
        nuevoCliente = clienteModel(clienteTipo=clienteTipo,clienteApellido = clienteApellido,clienteNombre=clienteNombre,clienteDocumento= clienteDocumento,clienteCelular=clienteCelular, clienteCorreo= clienteCorreo)
        nuevoCliente.set_password(clientePassword)
        nuevoCliente.save()
        return nuevoCliente
    class Meta:
        model = clienteModel
        exclude = [ 'groups','user_permissions', 'is_superuser',
                   'last_login', 'is_active', 'is_staff']
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
        extra_kwargs= {
            'cliente':{
                'write_only': True,    
            }
        }

# class AdoptadoSerializer(serializers.ModelSerializer):
#     clienteAdopcion=AdopcionSerializer(many=True)
#     class Meta:
#         model=AdopcionModel
class ClienteSerializer(serializers.ModelSerializer):
    
    clienteNombre=serializers.CharField(max_length=45, required=False,trim_whitespace=True,read_only=True)
   
    # clienteSexo=serializers.CharField(required=True,max_length=5)
    class Meta:
        model = clienteModel
        fields = '__all__'
        extra_kwargs= {
            'password':{
                'write_only': True,    
            },
            'is_active':{
                'write_only': True,    
            },
            'groups':{
                'write_only': True,    
            },
            'user_permissions':{
                'write_only': True,    
            },
            'is_staff':{
                'write_only': True,    
            },
            'clienteTipo':{
                'write_only': True,    
            }
        }

        
class Cliente_Estrella_Serializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    nombre = serializers.CharField(max_length=50,required=True)
    apellido = serializers.CharField(max_length=50,required=False, allow_blank=True)
    email = serializers.EmailField(max_length=50,required=True)
    documento = serializers.CharField(max_length=8,required=True)
    celular = serializers.CharField(max_length=9,required=False, allow_null=True)
    is_staff = serializers.BooleanField(required=True)
    cuenta = serializers.IntegerField(required=True)


        
class Producto_Estrella_Serializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    nombre = serializers.CharField(max_length=50,required=True)
    foto = serializers.CharField(max_length=50,required=True)
    precio = serializers.IntegerField(required=True)
    descripcion = serializers.CharField(max_length=200,required=True)
    
    cantidad = serializers.IntegerField(required=True)

        
class Producto_No_Estrella_Serializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    nombre = serializers.CharField(max_length=50,required=True)
    foto = serializers.CharField(max_length=50,required=True)
    precio = serializers.IntegerField(required=True)
    descripcion = serializers.CharField(max_length=200,required=True)
    
    cantidad = serializers.IntegerField(required=True)
    


class DetalleVentaSerializer(serializers.Serializer):
    cantidad = serializers.IntegerField(required=True)
    producto_id = serializers.IntegerField(required=True)
    


class VentaSerializer(serializers.Serializer):
    cliente_id = serializers.IntegerField(min_value=0, required=True)
    vendedor_id = serializers.IntegerField(min_value=0, required=True)
    detalle = DetalleVentaSerializer(many=True, required=True)

class FiltroPedidoSerializer(serializers.Serializer):
   
    class Meta:
        model=PedidoModel
        fields='__all__'
    





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
    productoFoto=serializers.CharField(max_length=100)
    class Meta:
        model = ProductoModel
        
        fields='__all__'
        

class DetallePedidoSerializer(serializers.ModelSerializer)  :
    producto = ProductoSerializer()
    class Meta:
        model=DetallePedidoModel
        fields='__all__'

class PedidoSerializer(serializers.ModelSerializer):
    pedidoDetalles=DetallePedidoSerializer(many=True)
    
    class Meta:
        model=PedidoModel
        fields='__all__'

class CustomPayloadSerializer(TokenObtainPairSerializer):
    # un funcion incorparada en python que devuelve un metodo de la clase de la cual se esta heredando
    # el metodo recibira la clase como primer argumento, cuando se llama a este metodo, se pasa a la clase como primer argumento en lugar de la instancia de la clase esto significa que puede utilizar la clase entera junto con sus propiedades dentro de este metodo sin tener que instanciar la clase   
    @classmethod
    def get_token(cls, user: clienteModel):
        token = super(CustomPayloadSerializer, cls).get_token(user)
        # print(token)
        token['user_email'] = user.clienteCorreo
        token['user_nombre'] = user.clienteNombre
        token['user_apellido'] = user.clienteApellido
        token["user_Tipo"] = user.clienteTipo
        return token
   