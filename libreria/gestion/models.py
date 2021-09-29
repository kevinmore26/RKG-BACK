from django.db.models.deletion import CASCADE
# from libreria import gestion
from django.db import models

# Create your models here.

class PerfilModel(models.Model):
    perfilId = models.AutoField(
        primary_key=True,null=False,unique=True,db_column='id'
    )
    perfilNick = models.CharField(
        db_column='nick',max_length=19
    )

class ClienteModel(models.Model):
    clienteId = models.AutoField(
        primary_key=True, null= False, unique= True, db_column='id'
    )
    clienteNombre = models.CharField(
         db_column='nombre',max_length=19
    )
    clienteDocumento = models.CharField(
         db_column='documento',max_length=8
    )
    clienteCelular = models.IntegerField(
        null=True,unique=True,db_column='celular'
    )
    perfilCliente = models.CharField(
         db_column='PerfilModel',max_length=19
    )
    
class ProductoModel(models.Model):

    class OpcionesUM(models.TextChoices):
        UNIDADES = 'UN', 'UNIDADES' 
        DOCENA = 'DOC', 'DOCENA' 
        CIENTO = 'CI', 'CIENTO' 
        MILLAR = 'MI', 'MILLAR' 


    # Tipos de datos del ORM => https://docs.djangoproject.com/en/3.2/ref/models/fields/#field-types
    # Parametros genericos de lo tipos de datos => https://docs.djangoproject.com/en/3.2/ref/models/fields/#field-options
    productoId = models.AutoField(
        primary_key=True, null=False, unique=True, db_column='id')

    productoNombre = models.CharField(
      db_column='nombre', null=False, max_length=14)

    productoPrecio = models.DecimalField(max_digits=5, decimal_places=2, db_column='precio')

    productoUnidadMedida = models.TextField(
        choices=OpcionesUM.choices, default=OpcionesUM.UNIDADES, db_column='unidad_medida')

    class Meta:
        """Link de documentacion https://docs.djangoproject.com/en/3.2/ref/models/options/"""
        db_table='productos'
        ordering = ['-productoPrecio']
        verbose_name = 'producto'
        verbose_name_plural = 'productos'
      
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
    clientes = models.ForeignKey(to=ClienteModel, db_column='clientes_id',
                                 null=False, related_name='clienteCabeceras', on_delete=models.PROTECT)

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
    productos = models.ForeignKey(to=ProductoModel, db_column='productos_id',
                                  on_delete=models.PROTECT, related_name='productoDetalles', null=False)
    
    cabeceras = models.ForeignKey(to=OrdenCabeceraModel, db_column='cabecera_operaciones_id',
                                  on_delete=models.PROTECT, related_name='cabeceraDetalles', null=False)

    class Meta:
        db_table = 'detalle_operaciones'
        verbose_name = 'detalle'
        verbose_name_plural = 'detalles'
