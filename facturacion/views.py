from rest_framework.generics import ListCreateAPIView
from .serializers import ComprobanteSerializer
from rest_framework.response import Response


class ComprobanteController(ListCreateAPIView):
    serializer_class = ComprobanteSerializer

    def post(self, request):
        data = self.serializer_class(data=request.data)
        if data.is_valid():
            print(data.validated_data)
            return Response(data={
                'message': ''
            }, status=201)
        else:
            return Response(data={
                'message': 'error al crear el comprobante',
                'content': data.errors
            }, status=400)

    def get(self, request):
        pass
