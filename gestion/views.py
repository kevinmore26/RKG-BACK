from typing import List
from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.files.base import equals_lf
from rest_framework.views import APIView
from django.db.models.query import QuerySet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from django.db import reset_queries, transaction, Error
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from .models import  ProductoModel, clienteModel,AdopcionModel,clienteModel,DetallePedidoModel,PedidoModel
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny, IsAdminUser,IsAuthenticated
from .serializers import (
                          VentaSerializer,
                          AdopcionSerializer,
                          ImagenSerializer,
                          RegistroSerializer,ProductoSerializer,
                          DetalleVentaSerializer,
                          Cliente_Estrella_Serializer,
                          PedidoSerializer,
                          ClienteSerializer,
                          Producto_Estrella_Serializer,
                          Producto_No_Estrella_Serializer,
                          
                          CustomPayloadSerializer)
from django.db import connection
                        
from rest_framework import status

from .utils import  PaginacionPersonalizada
# from .utils import PaginacionPersonalizada
from rest_framework.serializers import Serializer
# import requests as solicitudes
from os import environ
from django.db import transaction, Error
from datetime import datetime
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from os import remove
from django.db.models import ImageField
from django.conf import settings





        # -----------------------------------------------------------------------------------

class ProductosController(ListCreateAPIView):
    # pondremos la consulta de ese modelo en la bd
    queryset = ProductoModel.objects.all() #SELECT * FROM productos;
    serializer_class = ProductoSerializer
    
    def post(self, request: Request):
        # print(request.data)
        data = self.serializer_class(data=request.data)
        if data.is_valid():
            data.save()
            return Response(data={
                "message": "Producto creado exitosamente",
                "content": data.data
            }, status=status.HTTP_201_CREATED)
        else:
            return Response(data={
                "message": "Error al crear el producto",
                "content": data.errors
            }, status=status.HTTP_400_BAD_REQUEST)


    #! Get para solicitar solo productos de estado true

    def get(self, request):
        respuesta = self.get_queryset().filter(productoDisponible=True).all()
        print(respuesta)

        respuesta_serializada = self.serializer_class(
            instance=respuesta, many=True)

        return Response(data={
            "message": None,
            "content": respuesta_serializada.data
        })

class ProductoController(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductoSerializer
    queryset = ProductoModel.objects.all()


    def get(self, request, id):
        productoEncontrado = self.get_queryset().filter(productoId=id).first()

        if not productoEncontrado:
            return Response(data={
                'message': 'Producto no encontrado'
            },status=status.HTTP_404_NOT_FOUND)

        data = self.serializer_class(instance=productoEncontrado)

        return Response(data={
            'content': data.data
        })

    #! Delete para elimianar producto de la BD (comentado)
    # def delete(self, request, id):

    #     productoEncontrado = self.get_queryset().filter(productoId=id).first()
    #     if not productoEncontrado:
    #         return Response(data={
    #             'message': 'Producto no encontrado'
    #         }, status=status.HTTP_404_NOT_FOUND)

    #     try:
    #         data = productoEncontrado.delete()
    #         # print(str(productoEncontrado.productoFoto))
    #         remove(settings.MEDIA_ROOT / str(productoEncontrado.productoFoto))
    #     except Exception as e:
    #         print(e)
        
             
    #     # data = ProductoModel.objects.filter(productoId=id).delete()
    #     print(data)
    #     return Response(data={
    #         'message': 'Producto eliminado exitosamente'
    #     })

    def put(self, request: Request, id):
        #1 busco si el producto existe
        productoEncontrado = ProductoModel.objects.filter(
            productoId=id).first()

        if productoEncontrado is None:
            return Response(data={
                "message": "Producto no existe",
                "content": None
            }, status=status.HTTP_404_NOT_FOUND)

        #2 modifica los valores proveidos
        serializador = ProductoSerializer(data=request.data)
        if serializador.is_valid():
            serializador.update(instance=productoEncontrado, 
                                validated_data=serializador.validated_data)

            #3 guarda y devuelve el producto actualizado
            return Response(data={
                "message": "Producto actualizado exitosamente",
                "content": serializador.data
            })
        else:
            return Response(data={
                "message": "Error al actualizar el producto",
                "content": serializador.errors
            }, status=status.HTTP_400_BAD_REQUEST)

    #! Delete para cambiar a estado False al producto
    def delete(self, request, id):
        
        productoEncontrado: ProductoModel = ProductoModel.objects.filter(
            productoId=id).first()

        if productoEncontrado is None:
            return Response(data={
                "message": "Producto no encontrado",
                "content": None
            }, status=status.HTTP_404_NOT_FOUND)

        
        productoEncontrado.productoDisponible = False
        productoEncontrado.save()

        serializador = ProductoSerializer(instance=productoEncontrado)

        return Response(data={
            "message": "Producto eliminado exitosamente",
            "content": serializador.data
        })
       
        

class RegistroController (CreateAPIView):
    serializer_class = RegistroSerializer
    def post(self, request: Request):
        data = self.serializer_class(data = request.data)
        if data.is_valid():
            data.save()
            return Response(data={
                "message": "Usuario creado exitosamente",
                "content": data.data
            },)
        else:
            return Response(data={
                "message": "Error al crear el usuario",
                "content": data.errors
            })

class AdopcionesController(ListCreateAPIView):
    queryset = AdopcionModel.objects.all()
    serializer_class = AdopcionSerializer
    def post(self, request: Request):
        data = self.serializer_class(data=request.data)
        if data.is_valid():
            data.save()
            return Response(data={
                "message": "Adopcion creada exitosamente",
                "content": data.data
            }, status=status.HTTP_201_CREATED)
        else:
            return Response(data={
                "message": "Error al guardar la adopcion",
                "content": data.errors
            }, status=status.HTTP_400_BAD_REQUEST) 

class AdopcionController(RetrieveUpdateDestroyAPIView):
    serializer_class = AdopcionSerializer
    def get(self, request, id):
        
        adopcionEncontrada = AdopcionModel.objects.filter(
            adopcionId=id).first()
        try:
            adopcionEncontrada = AdopcionModel.objects.get(adopcionId=id)
            print(adopcionEncontrada)
        except AdopcionModel.DoesNotExist:
            print('No se encontro')

        if adopcionEncontrada is None:
            return Response(data={
                "message": "Adopcion no encontrada",
                "content": None
            }, status=status.HTTP_404_NOT_FOUND)
        
        serializador = AdopcionSerializer(instance=adopcionEncontrada)
        return Response(data={
            "message": "Adopcion encontrada",
            "content": serializador.data
        },status=status.HTTP_200_OK)

    def put(self, request: Request, id):
        # 1. busco si el producto existe
        adopcionEncontrada = AdopcionModel.objects.filter(
            adopcionId=id).first()

        if adopcionEncontrada is None:
            return Response(data={
                "message": "Adopcion no existe",
                "content": None
            }, status=status.HTTP_404_NOT_FOUND)

        
        serializador = AdopcionSerializer(data=request.data)
        if serializador.is_valid():
            serializador.update(instance=adopcionEncontrada,
                                validated_data=serializador.validated_data)
            
            return Response(data={
                "message": "Adopcion actualizada exitosamente",
                "content": serializador.data
            })
        else:
            return Response(data={
                "message": "Error al actualizar la adopcion",
                "content": serializador.errors
            }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):

        adopcionEncontrada: AdopcionModel = AdopcionModel.objects.filter(
            adopcionId=id).first()

        if adopcionEncontrada is None:
            return Response(data={
                "message": "Adopcion no encontrado",
                "content": None
            }, status=status.HTTP_404_NOT_FOUND)
        try:
            data=AdopcionModel.objects.filter(adopcionId=id).delete()
            adopcionEncontrada.delete()
            remove(settings.MEDIA_ROOT / str(adopcionEncontrada.adopcionFoto))
        except Exception as e:
            print(e)

        serializador = AdopcionSerializer(instance=adopcionEncontrada)
        return Response(data={
            "message": "Adopcion eliminado exitosamente",
            "content": serializador.data
        })


class BuscadorAdoptadoController(RetrieveAPIView):
    serializer_class = AdopcionSerializer

    def get(self, request: Request):
        nombre = request.query_params.get('nombre')
        estado = request.query_params.get('estado')
        animal = request.query_params.get('animal')
        id = request.query_params.get('id')
        adopcionEncontrado = None
        if id:
            adopcionEncontrado: QuerySet = AdopcionModel.objects.filter(
                adopcionId=id)

            # data = self.serializer_class(instance=clienteEncontrado, many=True)

            # return Response({'content': data.data})
        if estado:
            if adopcionEncontrado is not None:
                adopcionEncontrado = adopcionEncontrado.filter(
                    adopcionEstado__icontains=estado).all()
            else:
                adopcionEncontrado = AdopcionModel.objects.filter(
                    adopcionEstado__icontains=estado).all()

        if nombre:
            if adopcionEncontrado is not None:
                adopcionEncontrado = adopcionEncontrado.filter(
                    adopcionNombre__icontains=nombre).all()
            else:
                adopcionEncontrado = AdopcionModel.objects.filter(
                    adopcionNombre__icontains=nombre).all()

        

        data = self.serializer_class(instance=adopcionEncontrado, many=True)
        print(data.data)
        return Response(data={
            'message': 'Los adoptados son:',
            'content': data.data
        })

class SubirImagenController(CreateAPIView):
    serializer_class = ImagenSerializer

    def post(self, request: Request):
        print(request.FILES)
        data = self.serializer_class(data=request.FILES)

        if data.is_valid():
            archivo = data.save()
            url = request.META.get('HTTP_HOST')

            return Response(data={
                'message': 'Archivo subido exitosamente',
                'content': url + archivo
            }, status=status.HTTP_201_CREATED)
        else:
            return Response(data={
                'message': 'Error al crear el archivo',
                'content': data.errors
            }, status=status.HTTP_400_BAD_REQUEST)    
    
class VentaController(CreateAPIView):
    serializer_class = VentaSerializer

    def post(self, request):
        data = self.serializer_class(data=request.data)
        if data.is_valid():
            cliente_id = data.validated_data.get('cliente_id')
            vendedor_id = data.validated_data.get('vendedor_id')
            detalles = data.validated_data.get('detalle')
            try:
                with transaction.atomic():
                    cliente = clienteModel.objects.filter(
                        clienteId=cliente_id).first()

                    vendedor = clienteModel.objects.filter(
                        clienteId=vendedor_id).first()

                    if not cliente or not vendedor:
                        raise Exception('Usuarios incorrectos')

                    if cliente.clienteTipo != 3:
                        raise Exception('Cliente no corresponde el tipo')

                    if vendedor.clienteTipo == 3:
                        raise Exception('Vendedor no corresponde el tipo')

                    pedido = PedidoModel(
                        pedidoTotal=0, cliente=cliente, vendedor=vendedor)

                    pedido.save()
                    for detalle in detalles:
                        producto_id = detalle.get('producto_id')
                        cantidad = detalle.get('cantidad')
                        producto = ProductoModel.objects.filter(
                            productoId=producto_id).first()
                        if not producto:
                            raise Exception('Producto {} no existe'.format(
                                producto_id))
                        if cantidad > producto.productoCantidad:
                            raise Exception(
                                'No hay suficiente cantidad para el producto {}'.format(producto.productoNombre))
                        producto.productoCantidad = producto.productoCantidad - cantidad
                        producto.save()
                        detallePedido = DetallePedidoModel(detalleCantidad=cantidad,
                                                           detalleSubTotal=producto.productoPrecio * cantidad,
                                                           producto=producto,
                                                           pedido=pedido)
                        detallePedido.save()
                        pedido.pedidoTotal += detallePedido.detalleSubTotal
                        pedido.save()
                return Response(data={
                    'message': 'Venta agregada exitosamente'
                })

            except Exception as e:
                return Response(data={
                    'message': e.args
                }, status=400)

        else:
            return Response(data={
                'message': 'Error al agregar la venta',
                'content': data.errors
            })
# --------------------------------------
class BuscadorPedidoController(RetrieveAPIView):
    serializer_class = PedidoSerializer

    def get(self, request: Request):
        id = request.query_params.get('id')
        nombre = request.query_params.get('nombre')
        fecha = request.query_params.get('fecha')
        total = request.query_params.get('total')
        
        
        pedidoEncontrado = None
        if id:
            pedidoEncontrado: QuerySet = PedidoModel.objects.filter(
                pedidoId=id)

        if fecha:
            if pedidoEncontrado is not None:
                pedidoEncontrado = pedidoEncontrado.filter(
                    pedidoFecha__icontains=fecha).all()
            else:
                pedidoEncontrado = PedidoModel.objects.filter(
                    pedidoFecha__icontains=fecha).all()
        
        if total:
            if pedidoEncontrado is not None:
                pedidoEncontrado = pedidoEncontrado.filter(
                    pedidoTotal__icontains=total).all()
            else:
                pedidoEncontrado = PedidoModel.objects.filter(
                    pedidoTotal__icontains=total).all()

        data = self.serializer_class(instance=pedidoEncontrado, many=True)
        print(data.data)
        return Response(data={
            'message': 'Los pedidos son:',
            'content': data.data
        })
# ---------------------------------------
class BuscadorClienteController(RetrieveAPIView):
    serializer_class = ClienteSerializer
    permission_classes = [IsAdminUser]

    def get(self, request: Request):
        nombre = request.query_params.get('nombre')
        documento = request.query_params.get('documento')

        clienteEncontrado = None
        if documento:
            clienteEncontrado: QuerySet = clienteModel.objects.filter(
                clienteDocumento=documento)


        if nombre:
            if clienteEncontrado is not None:
                clienteEncontrado = clienteEncontrado.filter(
                    clienteNombre__icontains=nombre).all()
            else:
                clienteEncontrado = clienteModel.objects.filter(
                    clienteNombre__icontains=nombre).all()

        data = self.serializer_class(instance=clienteEncontrado, many=True)
        print(data.data)
        return Response(data={
            'message': 'Los usuarios son:',
            'content': data.data
        })

class OrdenesClienteController(RetrieveAPIView):
    serializer_class = PedidoSerializer
    def get(self, request:Request):
        ordenesEncontradas = None
        cliente_id = request.query_params.get('cliente_id')

        if cliente_id:
            if ordenesEncontradas is not None:
                ordenesEncontradas = ordenesEncontradas.objects.select_related().filter(cliente_id=cliente_id)
            else:
                ordenesEncontradas = PedidoModel.objects.select_related().filter(cliente_id=cliente_id)
        data = self.serializer_class(instance=ordenesEncontradas, many=True)
        return Response(data={
            'message':'Ordenes',
            'content':data.data
        })

class ClientesEspecialesController(APIView):
    # Cliente_Estrella_Serializer()
    serializer_class = Cliente_Estrella_Serializer
    permission_classes = [IsAdminUser]
    # print(serializer_class)
    def get(self,request):
        
        # lista_clientes = ()
        with connection.cursor() as cursor:
            cursor.execute('select t2.id,t2.nombre,t2.apellido,t2.email,t2.documento,t2.celular,t2.is_staff,count(*) as cuenta from public.pedidos t1 join public.clientes t2 on t1.cliente_id = t2.id where is_active = true group by t2.id,t2.nombre, t2.apellido,t2.email,t2.documento,t2.celular,t2.is_staff order by cuenta desc')
            resultado = cursor.fetchall()
            resultado_dic=[]
            for registro in resultado:
                diccionario = {
                    'id': registro[0],
                    'nombre':registro[1],
                    'apellido':registro[2],
                    'email':registro[3],
                    'documento':registro[4],
                    'celular':registro[5],
                    'is_staff':registro[6],
                    'cuenta':registro[7],
                }
                resultado_dic.append(diccionario)
            print(resultado)
            data = self.serializer_class(data= resultado_dic, many=True)
            data.is_valid(raise_exception=True)
            print(data.data)
            return Response(data={
            "message":None,
            "content":data.data
        })

class ProductosEspecialesController(APIView):
    # Cliente_Estrella_Serializer()
    serializer_class = Producto_Estrella_Serializer
    # print(serializer_class)
    def get(self,request):
        
        # lista_clientes = ()
        with connection.cursor() as cursor:
            cursor.execute('select t2.id,t2.nombre,t2.foto,t2.precio,t2.descripcion,t2.disponible,count(*) as cantidad from public.detalles t1 join public.productos t2 on t1.producto_id = t2.id where disponible = true group by t2.id,t2.nombre, t2.foto,t2.precio,t2.descripcion,t2.cantidad order by cantidad desc limit 1')
            resultado = cursor.fetchall()
            resultado_dic=[]
            for registro in resultado:
                diccionario = {
                    'id': registro[0],
                    'nombre':registro[1],
                    'foto':registro[2],
                    'precio':registro[3],
                    'descripcion':registro[4],
                    'disponible':registro[5],
                    'cantidad':registro[6],
                }
                resultado_dic.append(diccionario)
            print(resultado)
            data = self.serializer_class(data= resultado_dic, many=True)
            data.is_valid(raise_exception=True)
            print(data.data)
            return Response(data={
            "message":"El producto más vendido es 🧨",
            "content":data.data
        })

class ProductosNoEspecialesController(APIView):
    # Cliente_Estrella_Serializer()
    serializer_class = Producto_No_Estrella_Serializer
    # print(serializer_class)
    def get(self,request):
        
        # lista_clientes = ()
        with connection.cursor() as cursor:
            cursor.execute('select t2.id,t2.nombre,t2.foto,t2.precio,t2.descripcion,t2.disponible,count(*) as cantidad from public.detalles t1 join public.productos t2 on t1.producto_id = t2.id where disponible = true group by t2.id,t2.nombre, t2.foto,t2.precio,t2.descripcion,t2.cantidad order by cantidad asc limit 1')
            resultado = cursor.fetchall()
            resultado_dic=[]
            for registro in resultado:
                diccionario = {
                    'id': registro[0],
                    'nombre':registro[1],
                    'foto':registro[2],
                    'precio':registro[3],
                    'descripcion':registro[4],
                    'disponible':registro[5],
                    'cantidad':registro[6],
                }
                resultado_dic.append(diccionario)
            print(resultado)
            data = self.serializer_class(data= resultado_dic, many=True)
            data.is_valid(raise_exception=True)
            print(data.data)
            return Response(data={
            "message":"El producto menos vendido es 😥",
            "content":data.data
        })
class CustomPayloadController(TokenObtainPairView):
    """Sirve para modificar el payload de la token de acceso"""
    permission_classes = [AllowAny]
    serializer_class = CustomPayloadSerializer

    def post(self, request):
        data = self.serializer_class(data=request.data)
        print(data)
        if data.is_valid():
            print(data.validated_data)
            return Response(data={
                "success": True,
                "content": data.validated_data,
                "message": "Login exitoso"
            })

        else:
            return Response(data={
                "success": False,
                "content": data.errors,
                "message": "error de generacion de la jwt"
            })
class PerfilUsuario(RetrieveAPIView):
    
    permission_classes = [IsAuthenticated]
    
    # serializer_class = ClienteSerializer
    def get(self,request: Request ):            
            print(request.user)
            print(request.auth)
            data = {
                'clienteCorreo' : request.user.clienteCorreo,
                'clienteNombre': request.user.clienteNombre,
                'clienteApellido' : request.user.clienteApellido,
                'clienteTipo': request.user.clienteTipo
            }
            # data = self.serializer_class(data = request.data)
            return Response (data={
                'message':'El usuario es',
                'content':data
                #  request.user
            })
class ClienteActualizarController(RetrieveUpdateDestroyAPIView):           
    serializer_class = ClienteSerializer
    queryset = clienteModel.objects.all()
    
    def put(self, request: Request,id):
        clienteEncontrado = clienteModel.objects.filter(
            clienteId=id).first()

        if clienteEncontrado is None:
            return Response(data={
                "message": "Cliente no existe",
                "content": None
            }, status=status.HTTP_404_NOT_FOUND)

        
        serializador = ClienteSerializer(data=request.data)
        if serializador.is_valid():
            serializador.update(instance=clienteEncontrado, 
                                validated_data=serializador.validated_data)

           
            return Response(data={
                "message": "Cliente actualizado exitosamente",
                "content": serializador.data
            })
        else:
            return Response(data={
                "message": "Error al actualizar el cliente",
                "content": serializador.errors
            }, status=status.HTTP_400_BAD_REQUEST)