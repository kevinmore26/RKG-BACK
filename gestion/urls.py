from django.urls import path
from .views import (                  
                    OperacionController,
                    OperacionesController,
                    AdopcionesController,
                    AdopcionController,
                    SubirImagenController,
                    RegistroController,
                    ProductosController,
                    ProductoController)

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
                    
                    

urlpatterns = [
    
    path('operacion/', OperacionController.as_view()),
    path('operacion/<int:id>', OperacionesController.as_view()),
    path('adopciones/', AdopcionesController.as_view()),
    path('adopcion/<int:id>', AdopcionController.as_view()),
    path('subir-imagen', SubirImagenController.as_view()),
    path('cliente',RegistroController.as_view()),
    path('login', TokenObtainPairView.as_view()),
    path('refresh-session',TokenRefreshView.as_view()),
    path('productos/', ProductosController.as_view()),
    path('producto/<int:id>', ProductoController.as_view())
   
]



# ProductosController,
                    # ProductoController,
                    # ClienteController,
                    # BuscadorClienteController,

                     # path('productos/', ProductosController.as_view()),
    # path('producto/<int:id>', ProductoController.as_view()),
    # path('clientes/', ClienteController.as_view()),
    # path('buscar-cliente/', BuscadorClienteController.as_view()),