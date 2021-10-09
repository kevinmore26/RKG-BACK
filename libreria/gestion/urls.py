from django.urls import path
from .views import (RegistroContoller)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('cliente',RegistroContoller.as_view()),
    path('login', TokenObtainPairView.as_view()),
    path('refresh-session',TokenRefreshView.as_view()),
]
