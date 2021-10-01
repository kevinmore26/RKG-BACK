from django.urls import path
from .views import PruebaController, ProductosController


urlpatterns = [
    path('prueba/', PruebaController.as_view()),
    path('productos/', ProductosController.as_view()),
]