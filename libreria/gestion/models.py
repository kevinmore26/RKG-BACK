from django.db import models



class OrdenCabeceraModel(models.Model):
    # tipos = VENTA V | COMPRA C
    class OpcionesTipo(models.TextChoices):
        VENTA = 'V', 'VENTA'
        COMPRA = 'C', 'COMPRA'

    ordenCabeceraId = models.AutoField(
        db_column='id', primary_key=True, unique=True, null=False)

    ordenCabeceraFecha = models.DateTimeField(auto_now_add=True, db_column='fecha')

    ordenCabeceraTipo = models.TextField(
        choices=OpcionesTipo.choices, db_column='tipo', null=False)

    # ------------------------
    # clientes = models.ForeignKey(to=ClienteModel, db_column='clientes_id',
    #                              null=False, related_name='clienteCabeceras', on_delete=models.PROTECT)

    class Meta:
        db_table = 'cabecera_operaciones'
        verbose_name = 'ordencabecera'
        verbose_name_plural = 'ordencabeceras'


class OrdenDetalleModel(models.Model):
    ordenDetalleId = models.AutoField(
        db_column='id', primary_key=True, unique=True, null=False)

    ordenDetalleCantidad = models.IntegerField(db_column='cantidad', null=False)

    ordenDetalleImporte = models.DecimalField(
        max_digits=5, decimal_places=2, db_column='importe', null=False)
    # CAMBIAR RELATED_NAME
    # productos = models.ForeignKey(to=ProductoModel, db_column='productos_id',
    #                               on_delete=models.PROTECT, related_name='productoDetalles', null=False)
    
    # cabeceras = models.ForeignKey(to=CabeceraModel, db_column='cabecera_operaciones_id',
    #                               on_delete=models.PROTECT, related_name='cabeceraDetalles', null=False)

    class Meta:
        db_table = 'detalle_operaciones'
        verbose_name = 'detalle'
        verbose_name_plural = 'detalles'
