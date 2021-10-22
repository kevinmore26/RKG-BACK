from django.urls import path
from django.urls.conf import re_path
from .views import (                  
                    
                    AdopcionesController,
                    AdopcionController,
                    SubirImagenController,
                    RegistroController,
                    ProductosController,
                    ProductoController,
                    VentaController,
                    BuscadorAdoptadoController,
                    BuscadorPedidoController,
                    BuscadorClienteController,
                    ClientesEspecialesController,
                    OrdenesClienteController,
                    ProductosEspecialesController,
                    ProductosNoEspecialesController,
                    CustomPayloadController,
                    PerfilUsuario,
                    ClienteActualizarController)

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView,TokenVerifyView
                    
                    

urlpatterns = [
    
    path('registro', RegistroController.as_view()),
    path('login',CustomPayloadController.as_view()),
    path('virify-toke',TokenVerifyView.as_view()),
    path('perfil_cliente',PerfilUsuario.as_view()),
    path('actualizar-cliente/<int:id>', ClienteActualizarController.as_view()),
    path('buscar-cliente/', BuscadorClienteController.as_view()),
    path('cliente_especial',ClientesEspecialesController.as_view()),
    path('login', TokenObtainPairView.as_view()),
    path('adopciones/', AdopcionesController.as_view()),
    path('adopcion/<int:id>', AdopcionController.as_view()),
    path('buscar-adoptado/',BuscadorAdoptadoController.as_view()),
    path('subir-imagen/', SubirImagenController.as_view()),  
    path('refresh-session',TokenRefreshView.as_view()),
    path('productos/', ProductosController.as_view()),
    path('producto/<int:id>', ProductoController.as_view()),
    path('buscar-pedido', BuscadorPedidoController.as_view()),
    path('buscar-orden-cliente', OrdenesClienteController.as_view()),
    path('producto-estrella', ProductosEspecialesController.as_view()),
    path('producto-no-estrella', ProductosNoEspecialesController.as_view()),
    path('pedido', VentaController.as_view()),
   
]



