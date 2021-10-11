from django.contrib import admin
from .models import clienteModel, ProductoModel,AdopcionModel

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['productoId', 'productoNombre', 'productoPrecio', 'productoUnidadMedida', 'productoDescripcion']

    search_fields = ['productoNombre', 'productoDescripcion']

    # list_filter = [productoTipo]

    readonly_fields = ['productoId']





class ProductoAdmin(admin.ModelAdmin):
    
    list_display = ['productoId', 'productoNombre', 'productoPrecio']
    
    search_fields = ['productoNombre']
    
  
    
    readonly_fields = ['productoId']


class AdopcionesAdmin(admin.ModelAdmin):
    list_display = ['adopcionId', 'adopcionNombre', 'adopcionEdad',]
    search_fields = ['adopcionNombre', 'adopcionTamanio']
    list_filter = ['adopcionTamanio']
    readonly_fields = ['productoId']


admin.site.register(clienteModel)
admin.site.register(ProductoModel, ProductoAdmin)
admin.site.register(AdopcionModel)

