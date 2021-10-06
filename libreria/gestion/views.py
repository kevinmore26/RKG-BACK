from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import ProductoModel
from rest_framework import status
from .serializers import ProductoSerializer, ImagenSerializer
from rest_framework import status
from .utils import  PaginacionPersonalizada
from os import remove
from django.conf import settings
 

class PruebaController(APIView):
    def get(self, request, format=None):
        return Response(data={'message': 'Exito'}, status=200)

    def post(self, request:Request, format=None):
        print(request.data)
        return Response(data={'message': 'Hiciste post'})

class ProductosController(ListCreateAPIView):
    # pondremos la consulta de ese modelo en la bd
    queryset = ProductoModel.objects.all() #SELECT * FROM productos;
    serializer_class = ProductoSerializer
    pagination_class = PaginacionPersonalizada



    def get(self, request):
        data = self.serializer_class(instance=self.get_queryset(), many=True)
        return Response(data={
            "message": None,
            "content": data.data
        })

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
                "message": "Error al crear el producto",
                "content": data.errors
            }, status=status.HTTP_400_BAD_REQUEST)




    #Todo comentado para que funcione la paginacion / desactivar para que funcione listado de productos (get)



    # def get(self, request):
    #     respuesta = self.get_queryset().filter(productoEstado=True).all()
    #     print(respuesta)
    #     respuesta_serializada = self.serializer_class(
    #         instance=respuesta, many=True)
    #     return Response(data={
    #         "message": None,
    #         "content": respuesta_serializada.data
    #     })
    


class ProductoController(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductoSerializer
    queryset = ProductoModel.objects.all()


    # def patch(self, request, id):
    #     # actualizacion parcial
    #     pass

    # def put(self, request, id):
    #     # actualizacion total
    #     pass

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


    def delete(self, request, id):

        productoEncontrado = self.get_queryset().filter(productoId=id).first()
        if not productoEncontrado:
            return Response(data={
                'message': 'Producto no encontrado'
            }, status=status.HTTP_404_NOT_FOUND)

        try:
            data = productoEncontrado.delete()
            # print(str(productoEncontrado.productoFoto))
            remove(settings.MEDIA_ROOT / str(productoEncontrado.productoFoto))
        except Exception as e:
            print(e)
        
             
        # data = ProductoModel.objects.filter(productoId=id).delete()
        print(data)
        return Response(data={
            'message': 'Producto eliminado exitosamente'
        })


    # def get(self, request, id):
    #     # SELECT * FROM productos WHERE id = id
    #     productoEncontrado = ProductoModel.objects.filter(
    #         productoId=id).first()
    #     try:
    #         productoEncontrado2 = ProductoModel.objects.get(productoId=id)
    #         print(productoEncontrado2) 
    #     except ProductoModel.DoesNotExist:
    #         print('No se encontro')

    #     #si el producto no existe retornar message='producto no existe' con un estado NOT_FOUND
    #     if productoEncontrado is None:
    #         return Response(data={
    #             "message": "Producto no encontrado",
    #             "content": None
    #         }, status=status.HTTP_404_NOT_FOUND)

    #     serializador = ProductoSerializer(instance=productoEncontrado)
    #     return Response(data={
    #         "message": None,
    #         "content": serializador.data
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

class SubirImagenController(CreateAPIView):
    serializer_class= ImagenSerializer

    def post(self, request:Request):
        print(request.FILES)
        data = self.serializer_class(data= request.FILES)

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
