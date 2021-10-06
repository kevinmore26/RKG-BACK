from typing import List
from django.shortcuts import render
from rest_framework.views import APIView
from django.db.models.query import QuerySet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from .models import  ProductoModel, clienteModel,AdopcionModel,clienteModel,DetallePedidoModel,PedidoModel
from .serializers import (
                          VentaSerializer,
                          AdopcionSerializer,
                          ImagenSerializer,
                          RegistroSerializer,ProductoSerializer)
                        
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




class PruebaController(APIView):
    def get(self, request, format=None):
        return Response(data={'message': 'Exito'}, status=200)

    def post(self, request: Request, format=None):
        print(request.data)
        return Response(data={'message': 'Hiciste post'})
class ProductosController(ListCreateAPIView):
    # pondremos la consulta de ese modelo en la bd
    queryset = ProductoModel.objects.all() #SELECT * FROM productos;
    serializer_class = ProductoSerializer
    pagination_class = PaginacionPersonalizada

    #Todo comentado para que funcione la paginacion / desactivar para que funcione listado de productos

    # def get(self, request):
    #     respuesta = self.get_queryset().filter(productoEstado=True).all()
    #     print(respuesta)
    #     respuesta_serializada = self.serializer_class(
    #         instance=respuesta, many=True)
    #     return Response(data={
    #         "message": None,
    #         "content": respuesta_serializada.data
    #     })
    
    def post(self, request: Request):
        print(request.data)
        data = self.serializer_class(data=request.data)
        if data.is_valid():
            data.save()
            return Response(data={
                "message": "Producto creado exitosamente",
                "content": data.data
            }, status=status.HTTP_201_CREATED)
        else:
            return Response(data={
                "message": "Error al guardar el producto",
                "content": data.errors
            }, status=status.HTTP_400_BAD_REQUEST)

class ProductoController(APIView):

    def get(self, request, id):
        # SELECT * FROM productos WHERE id = id
        productoEncontrado = ProductoModel.objects.filter(
            productoId=id).first()
        try:
            productoEncontrado2 = ProductoModel.objects.get(productoId=id)
            print(productoEncontrado2) 
        except ProductoModel.DoesNotExist:
            print('No se encontro')

        #si el producto no existe retornar message='producto no existe' con un estado NOT_FOUND
        if productoEncontrado is None:
            return Response(data={
                "message": "Producto no encontrado",
                "content": None
            }, status=status.HTTP_404_NOT_FOUND)

        serializador = ProductoSerializer(instance=productoEncontrado)
        return Response(data={
            "message": None,
            "content": serializador.data
        })

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

    def delete(self, request, id):

        productoEncontrado: ProductoModel = ProductoModel.objects.filter(
            productoId=id).first()

        if productoEncontrado is None:
            return Response(data={
                "message": "Producto no encontrado",
                "content": None
            }, status=status.HTTP_404_NOT_FOUND)

        productoEncontrado.productoEstado = False
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
            })
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
    def get(self, request, id):
        
        adopcionEncontrada = AdopcionModel.objects.filter(
            adopcionId=id).first()
        try:
            adopcionEncontrada2 = AdopcionModel.objects.get(adopcionId=id)
            print(adopcionEncontrada2)
        except AdopcionModel.DoesNotExist:
            print('No se encontro')

        if adopcionEncontrada is None:
            return Response(data={
                "message": "Adopcion no encontrada",
                "content": None
            }, status=status.HTTP_404_NOT_FOUND)

        serializador = AdopcionSerializer(instance=adopcionEncontrada)
        return Response(data={
            "message": None,
            "content": serializador.data
        })

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

