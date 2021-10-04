from django.urls import path
from .views import (ClienteContoller)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('cliente',ClienteContoller.as_view()),
    path('login', TokenObtainPairView.as_view()),
    path('refresh-session',TokenRefreshView.as_view()),
]
