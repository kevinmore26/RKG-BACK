from django.db.models.deletion import CASCADE
from django.db import models
from .authManager import ManejoCliente
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser
from django.core.validators import MinValueValidator



class PerfilModel(models.Model):
    perfilId = models.AutoField(
        primary_key=True,null=False,unique=True,db_column='id'
    )
    perfilNick = models.CharField(
        db_column='nick',max_length=19
    )

class ProductoModel(models.Model):

        

    # Tipos de datos del ORM => https://docs.djangoproject.com/en/3.2/ref/models/fields/#field-types
    # Parametros genericos de lo tipos de datos => https://docs.djangoproject.com/en/3.2/ref/models/fields/#field-options
    productoId = models.AutoField(
        primary_key=True, null=False, unique=True, db_column='id')

    productoNombre = models.CharField(
      db_column='nombre', null=False, max_length=50, verbose_name='nombre')
    
    productoPrecio = models.DecimalField(
        max_digits=9, decimal_places=2, db_column='precio', verbose_name='precio')

    productoDescripcion = models.CharField(
        db_column='descripcion', null=False, max_length=100, verbose_name='descripcion')
    
    productoFoto = models.ImageField(
        upload_to='productos/', db_column='foto', null=True)

    productoCantidad = models.IntegerField(
        db_column='cantidad', null=False, default=0)

    productoDisponible = models.BooleanField(
        db_column='disponible', default=True, null=False)

    # se actualizara su valor cuando el registro sufra alguna modificacion
    # auto_now => agarrara la fecha actual cuando parte del registro o en su totalidad sea modificada
    updatedAt = models.DateField(db_column='updated_at', auto_now=True)

    # auto_now_add => cuando se cree un nuevo registro, agarrara la fecha actual y lo creara en esta columna
    createdAt = models.DateField(db_column='created_at', auto_now_add=True)

    def __str__(self):
        return self.productoNombre

    class Meta:
        """Link de documentacion https://docs.djangoproject.com/en/3.2/ref/models/options/"""
        db_table='productos'
        ordering = ['-productoPrecio']
        verbose_name = 'producto'
        verbose_name_plural = 'productos'



class clienteModel(AbstractBaseUser, PermissionsMixin):
    
    TIPO_USUARIO = [(1, 'ADMINISTRADOR'), (2, 'MIEMBRO'), (3, 'CLIENTE')]

    clienteId = models.AutoField(
        primary_key=True, db_column='id', unique=True, null=False)

    clienteNombre = models.CharField(max_length=50, db_column='nombre',verbose_name='Nombre del usuario')

    clienteApellido = models.CharField(
        max_length=50, db_column='apellido', verbose_name='Apellido del usuario')

    clienteCorreo = models.EmailField(
        max_length=50, db_column='email', unique=True)

    clienteTipo = models.IntegerField(choices=TIPO_USUARIO, db_column='tipo',null=False)

    clienteDocumento = models.CharField(
         db_column='documento',max_length=9,unique=False
    )
    clienteCelular = models.IntegerField(
        null=True,unique=True,db_column='celular'
    )
    password = models.TextField(null=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = ManejoCliente()

    USERNAME_FIELD = 'clienteCorreo'

    # es lo que pedira la consola cuando se llame al createsuperuser
    REQUIRED_FIELDS = ['clienteNombre', 'clienteApellido', 'clienteTipo','clienteDocumento','clienteCelular']

    class Meta:
        db_table = 'clientes'


class PedidoModel(models.Model):
    pedidoId = models.AutoField(primary_key=True, db_column='id', unique=True)

    pedidoFecha = models.DateField(auto_now_add=True, db_column='fecha')

    pedidoTotal = models.DecimalField(
        max_digits=9, decimal_places=2, db_column='total')

    cliente = models.ForeignKey(
        to=clienteModel, related_name='clientePedidos', db_column='cliente_id', on_delete=models.PROTECT)

    vendedor = models.ForeignKey(
        to=clienteModel, related_name='vendedorPedidos', db_column='vendedor_id', on_delete=models.PROTECT)

    class Meta:
        db_table = 'pedidos'



class DetallePedidoModel(models.Model):
    detalleId = models.AutoField(primary_key=True, db_column='id', unique=True)

    detalleCantidad = models.IntegerField(
        db_column='cantidad', null=False, validators=[MinValueValidator(0, 'Valor no puede ser negativo')])

    detalleSubTotal = models.DecimalField(
        max_digits=9, decimal_places=2, db_column='sub_total')

    producto = models.ForeignKey(
        to=ProductoModel, related_name='productoDetalles', db_column='producto_id', on_delete=models.PROTECT)
    
    pedido = models.ForeignKey(
        to=PedidoModel, related_name='pedidoDetalles', db_column='pedido_id', on_delete=models.PROTECT)

    class Meta:
        db_table = 'detalles'



class AdopcionModel(models.Model):

    class OpcionesUM(models.TextChoices):
        PEQUEÑO = 'P', 'PEQUEÑO' 
        MEDIANO = 'M', 'MEDIANO' 
        GRANDE = 'G', 'GRANDE' 

    estadoAdoptado = [(1,'ADOPTADO'),(2,'NO_ADOPTADO')]


    adopcionId = models.AutoField(
        primary_key=True, null=False, unique=True, db_column='id')

    adopcionNombre = models.CharField(
      db_column='nombre', null=False, max_length=14)
    
    adopcionEdad = models.IntegerField(null=True,db_column='edad')

    adopcionTamanio = models.TextField(
        choices=OpcionesUM.choices, default=OpcionesUM.MEDIANO, db_column='tamanio')
    
    adopcionCaracteristicas = models.CharField(
      db_column='caracteristicas', null=False, max_length=100)

    adopcionFoto = models.ImageField(
        upload_to='adopciones/', db_column='foto', null=True)
    
    adopcionEstado=models.BooleanField(
        db_column='estado', default=True, null=False)
    

    # place = models.OneToOneField(
    #     Place,
    #     on_delete=models.CASCADE,
    #     primary_key=True,
    # )
    cliente = models.ForeignKey(to=clienteModel,db_column='cliente_id',
                                  on_delete=models.PROTECT,related_name='clienteAdopcion',null=True, blank=True)
    

    class Meta:
        
        db_table='adopciones'
        ordering = ['-adopcionTamanio']
        verbose_name = 'adopcion'
        verbose_name_plural = 'adopciones'