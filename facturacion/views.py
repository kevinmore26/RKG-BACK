from rest_framework.generics import ListCreateAPIView

from .models import ComprobanteModel
from .serializers import ComprobanteSerializer, ComprobanteModelSerializer
from rest_framework.response import Response
from .generarComprobante import crearComprobante


class ComprobanteController(ListCreateAPIView):
    serializer_class = ComprobanteSerializer

    def post(self, request):
        data = self.serializer_class(data=request.data)
        if data.is_valid():
            print(data.validated_data)
            tipoComprobante = data.validated_data.get('tipoComprobante')
            pedidoId = data.validated_data.get('pedidoId')
            numeroDocumento = data.validated_data.get('numeroDocumento')

            tipoComprobante = 2 if tipoComprobante == 'BOLETA' else 1

            respuesta = crearComprobante(
                tipoComprobante, pedidoId, numeroDocumento)
            if isinstance(respuesta, ComprobanteModel):
                data = ComprobanteModelSerializer(instance=respuesta)

                return Response(data={
                    'message': 'Comprobante Generado exitosamente',
                    'content': data.data

                }, status=201)
            else:
                return Response(data={
                    'message': 'Error al crear el comprobante',
                    'content': respuesta
                }, status=400)
        else:
            return Response(data={
                'message': 'error al crear el comprobante',
                'content': data.errors
            }, status=400)

    def get(self, request):
        pass
