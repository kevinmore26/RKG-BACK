from django.shortcuts import render
from rest_framework.views import APIView

class PruebaController(APIView):
    def get(self, request):
        return {'message': 'Exito'}

