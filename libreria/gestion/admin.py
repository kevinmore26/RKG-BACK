from django.contrib import admin
from .models import ClienteModel, ProductoModel,AdopcionModel

class ProductoAdmin(admin.ModelAdmin):
    
    list_display = ['productoId', 'productoNombre', 'productoPrecio']
    
    search_fields = ['productoNombre', 'productoUnidadMedida']
    
    list_filter = ['productoUnidadMedida']
    
    readonly_fields = ['productoId']


class AdopcionesAdmin(admin.ModelAdmin):
    list_display = ['adopcionId', 'adopcionNombre', 'adopcionEdad',]
    search_fields = ['adopcionNombre', 'adopcionTamaño']
    list_filter = ['adopcionTamaño']
    readonly_fields = ['productoId']


admin.site.register(ClienteModel)
admin.site.register(ProductoModel, ProductoAdmin)
admin.site.register(AdopcionModel)

