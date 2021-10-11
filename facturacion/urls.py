from django.urls import path
from .views import ComprobanteController

urlpatterns = [
    path('generar-comprobante/', ComprobanteController.as_view()),
]

