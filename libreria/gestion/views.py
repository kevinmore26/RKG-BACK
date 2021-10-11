from django.db.models.query_utils import select_related_descend
from django.shortcuts import render
from rest_framework import response, status
from rest_framework.generics import CreateAPIView, ListCreateAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from .serializador import  RegistroSerializer
# from .models import PlatoModel


class RegistroContoller (CreateAPIView):
    serializer_class = RegistroSerializer
    def post(self, request: Request):
        data = self.serializer_class(data = request.data)
        if data.is_valid():
            data.save()
            return Response(data={
                "message": "Usuario creado exitosamente",
                "content": data.data
            })
        else:
            return Response(data={
                "message": "Error al crear el usuario",
                "content": data.errors
            })