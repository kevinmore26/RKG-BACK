from django.urls import path
from .views import PruebaController


urlpatterns = [
    path('prueba/', PruebaController.as_view())
]