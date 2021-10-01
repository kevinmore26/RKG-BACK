from django.urls import path
from .views import (                  
                    OperacionController,
                    OperacionesController,
                    AdopcionesController,
                    AdopcionController)
                    

urlpatterns = [
    
    path('operacion/', OperacionController.as_view()),
    path('operacion/<int:id>', OperacionesController.as_view()),
    path('adopciones/', AdopcionesController.as_view()),
    path('adopcion/<int:id>', AdopcionController.as_view()),
   
]



# ProductosController,
                    # ProductoController,
                    # ClienteController,
                    # BuscadorClienteController,

                     # path('productos/', ProductosController.as_view()),
    # path('producto/<int:id>', ProductoController.as_view()),
    # path('clientes/', ClienteController.as_view()),
    # path('buscar-cliente/', BuscadorClienteController.as_view()),