from django.db.models.deletion import CASCADE
from django.db import models



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
    clienteCorreo = models.EmailField(
        max_length=50, db_column='email', unique= True,null=False,default='rkg@mascotitas.com'
    )
    clientePassword = models.TextField(null=True)
    clienteCelular = models.IntegerField(
        null=True,unique=True,db_column='celular'
    )
    
    perfilCliente = models.CharField(
         db_column='PerfilModel',max_length=19
    )
    perfiles = models.ForeignKey(to=PerfilModel, db_column='perfiles_id',
                                 null=False, related_name='perfilCliente0', on_delete=models.PROTECT)
    USERNAME_FIELD = 'clienteCorreo'
    class Meta:
        db_table = 'clientes'
        verbose_name = 'cliente'
        verbose_name_plural = 'clientes'
class ProductoModel(models.Model):

    class OpcionesUM(models.TextChoices):
        UNIDAD = 'UN', 'UNIDAD' 
        


    # Tipos de datos del ORM => https://docs.djangoproject.com/en/3.2/ref/models/fields/#field-types
    # Parametros genericos de lo tipos de datos => https://docs.djangoproject.com/en/3.2/ref/models/fields/#field-options
    productoId = models.AutoField(
        primary_key=True, null=False, unique=True, db_column='id')

    productoNombre = models.CharField(
      db_column='nombre', null=False, max_length=50, verbose_name='nombre')

    productoPrecio = models.DecimalField(
        max_digits=5, decimal_places=2, db_column='precio', verbose_name='precio')

    productoUnidadMedida = models.TextField(
        choices=OpcionesUM.choices, default=OpcionesUM.UNIDAD, db_column='unidad_medida', verbose_name='UnidadMedida')

    productoDescripcion = models.CharField(
        db_column='descripcion', null=False, max_length=100, verbose_name='descripcion',default='none' )
    
    productoEstado = models.BooleanField(db_column='estado', default=True, null=False)

    def __str__(self):
        return self.productoNombre

    class Meta:
        """Link de documentacion https://docs.djangoproject.com/en/3.2/ref/models/options/"""
        db_table='productos'
        ordering = ['-productoPrecio']
        verbose_name = 'producto'
        verbose_name_plural = 'productos'



# ORDEN_CABECERA
class CabeceraModel(models.Model):
    # tipos = VENTA V | COMPRA C
    class OpcionesTipo(models.TextChoices):
        VENTA = 'V', 'VENTA'
        COMPRA = 'C', 'COMPRA'

    cabeceraId = models.AutoField(
        db_column='id', primary_key=True, unique=True, null=False)

    cabeceraFecha = models.DateTimeField(auto_now_add=True, db_column='fecha')

    cabeceraTipo = models.TextField(
        choices=OpcionesTipo.choices, db_column='tipo', null=False)

   
    clientes = models.ForeignKey(to=ClienteModel, db_column='clientes_id',
                                 null=False, related_name='clienteCabeceras', on_delete=models.PROTECT)

    class Meta:
        db_table = 'cabecera_operaciones'
        verbose_name = 'cabecera'
        verbose_name_plural = 'cabeceras'


class DetalleModel(models.Model):
    detalleId = models.AutoField(
        db_column='id', primary_key=True, unique=True, null=False)

    detalleCantidad = models.IntegerField(db_column='cantidad', null=False)

    detalleImporte = models.DecimalField(
        max_digits=5, decimal_places=2, db_column='importe', null=False)

    productos = models.ForeignKey(to=ProductoModel, db_column='productos_id',
                                  on_delete=models.PROTECT, related_name='productoDetalles', null=False)

    cabeceras = models.ForeignKey(to=CabeceraModel, db_column='cabecera_operaciones_id',
                                  on_delete=models.PROTECT, related_name='cabeceraDetalles', null=False)

    class Meta:
        db_table = 'detalle_operaciones'
        verbose_name = 'detalle'
        verbose_name_plural = 'detalles'
class AdopcionModel(models.Model):

    class OpcionesUM(models.TextChoices):
        PEQUEÑO = 'P', 'PEQUEÑO' 
        MEDIANO = 'M', 'MEDIANO' 
        GRANDE = 'G', 'GRANDE' 
    adopcionId = models.AutoField(
        primary_key=True, null=False, unique=True, db_column='id')

    adopcionNombre = models.CharField(
      db_column='nombre', null=False, max_length=14)
    
    adopcionEdad = models.IntegerField(null=True,db_column='edad')

    adopcionTamaño = models.TextField(
        choices=OpcionesUM.choices, default=OpcionesUM.MEDIANO, db_column='tamanio')
    
    adopcionCaracteristicas = models.CharField(
      db_column='caracteristicas', null=False, max_length=100)

    adopcionFoto = models.ImageField(
        upload_to='adopciones/', db_column='foto', null=True)
    

    # place = models.OneToOneField(
    #     Place,
    #     on_delete=models.CASCADE,
    #     primary_key=True,
    # )
    clientes = models.ForeignKey(to=ClienteModel,db_column='cliente_id',
                                  on_delete=models.PROTECT,related_name='clienteAdopcion',null=True, blank=True)

    class Meta:
        
        db_table='adopciones'
        ordering = ['-adopcionTamaño']
        verbose_name = 'adopcion'
        verbose_name_plural = 'adopciones'