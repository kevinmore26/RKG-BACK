from django.urls import path
from .views import (ProductoController,
                    PruebaController,
                    ProductosController, 
                    SubirImagenController)


urlpatterns = [
    path('prueba/', PruebaController.as_view()),
    path('productos/', ProductosController.as_view()),
    path('producto/<int:id>', ProductoController.as_view()),
    path('subir-imagen/', SubirImagenController.as_view())
]