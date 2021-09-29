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
    
