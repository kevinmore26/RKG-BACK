from django.shortcuts import render
from rest_framework.views import APIView
from django.db.models.query import QuerySet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from .models import CabeceraModel, DetalleModel, ProductoModel, ClienteModel
# from .serializers import (ProductoSerializer,
                        #   ClienteSerializer,
                        #   OperacionSerializer,
                        #   OperacionModelSerializer)
from rest_framework import status
# from .utils import PaginacionPersonalizada
from rest_framework.serializers import Serializer
# import requests as solicitudes
from os import environ
from django.db import transaction, Error
from datetime import datetime
from django.shortcuts import get_object_or_404
from rest_framework.response import Response




class PruebaController(APIView):
    def get(self, request, format=None):
        return Response(data={'message': 'Exito'}, status=200)

    def post(self, request: Request, format=None):
        print(request.data)
        return Response(data={'message': 'Hiciste post'})