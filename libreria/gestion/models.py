from django.db import models


#https://docs.djangoproject.com/en/3.2/ref/models/
#https://docs.djangoproject.com/en/3.2/topics/db/models/

class ProductoModel(models.Model):
    # Tipos de datos del ORM => https://docs.djangoproject.com/en/3.2/ref/models/fields/#field-types
    # Parametros genericos de lo tipos de datos => https://docs.djangoproject.com/en/3.2/ref/models/fields/#field-options
    productoId = models.AutoField(
        primary_key=True, null=False, unique=True, db_column='id')

    productoNombre = models.CharField(
      max_length=45, db_column='nombre', null=False)  
    