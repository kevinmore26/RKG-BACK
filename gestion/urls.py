from django.urls import path
from .views import (                  
                    
                    AdopcionesController,
                    AdopcionController,
                    SubirImagenController,
                    RegistroController,
                    ProductosController,
                    ProductoController,
                    VentaController,
                    BuscadorAdoptadoController)

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
                    
                    

urlpatterns = [
    
    path('registro', RegistroController.as_view()),
    path('login', TokenObtainPairView.as_view()),
    path('adopciones/', AdopcionesController.as_view()),
    path('adopcion/<int:id>', AdopcionController.as_view()),
    path('buscar-adoptado/',BuscadorAdoptadoController.as_view()),
    path('subir-imagen/', SubirImagenController.as_view()),  
    path('refresh-session',TokenRefreshView.as_view()),
    path('productos/', ProductosController.as_view()),
    path('producto/<int:id>', ProductoController.as_view()),
    path('pedido', VentaController.as_view()),
   
]



