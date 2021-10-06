from datetime import datetime
from .models import ComprobanteModel
from gestion.models import PedidoModel
from django.db import connection


def crearComprobante(tipo_de_comprobante: int, pedido: PedidoModel, documento_cliente: str):
    operacion = 'generar_comprobante'
    if tipo_de_comprobante == 1:
        serie = 'FFF1'  # *
    elif tipo_de_comprobante == 2:
        serie = 'BBB1'

    ultimoComprobante = ComprobanteModel.objects.values_list('comprobanteNumero').filter(
        comprobanteSerie=serie).order_by('-comprobanteNumero').first()

    if not ultimoComprobante:
        numero = 1
    else:
        numero = ultimoComprobante.comprobanteNumero + 1
    sunat_transaction = 1  # *

    cliente_tipo_de_documento = (
        1 if len(documento_cliente) == 8 else 6) if documento_cliente else 6

    cliente_numero_de_documento = documento_cliente

    cliente_denominacion = pedido.cliente.clienteNombre + \
        ' '+pedido.cliente.clienteApellido
    cliente_direccion = ''
    cliente_email = pedido.cliente.clienteCorreo
    fecha_de_emision = datetime.now()
    moneda = 1
    porcentaje_de_igv = 18
    total = pedido.pedidoTotal
    formato_de_pdf = 'TICKET'


def visualizarComprobante():
    pass


