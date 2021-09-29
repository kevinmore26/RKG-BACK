from django.db.models.deletion import CASCADE
from libreria import gestion
from django.db import models

# Create your models here.

class PerfilModel(models.Model):
    perfilId = models.AutoField(
        primary_key=True,null=False,unique=True,db_column='id'
    )
    perfilNick = models.CharField(
        max_length=45,db_column='nick'
    )

class ClienteModel(models.Model):
    clienteId = models.AutoField(
        primary_key=True, null= False, unique= True, db_column='id'
    )
    clienteNombre = models.CharField(
        max_length=45, db_column='nombre'
    )
    clienteDocumento = models.CharField(
        max_length=45, db_column='documento'
    )
    clienteCelular = models.AutoField(
        primary_key=False, null=True,unique=True,db_column='celular'
    )
    # perfilCliente = models.ForeignKey(
    #      'PerfilModel', on_delete=models.CASCADE
    # )
    
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
      max_length=45, db_column='nombre', null=False)

    productoPrecio = models.DecimalField(max_digits=5, decimal_places=2, db_column='precio')

    productoUnidadMedida = models.TextField(
        choices=OpcionesUM.choices, default=OpcionesUM.UNIDADES, db_column='unidad_medida')

    class Meta:
        """Link de documentacion https://docs.djangoproject.com/en/3.2/ref/models/options/"""
        db_table='productos'
        ordering = ['-productoPrecio']
        verbose_name = 'producto'
        verbose_name_plural = 'productos'
      

# class 
