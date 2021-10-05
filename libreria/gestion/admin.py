from django.contrib import admin
from .models import ClienteModel, ProductoModel

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['productoId', 'productoNombre', 'productoPrecio','productoDescripcion']

    search_fields = ['productoNombre', 'productoDescripcion']

    # list_filter = [productoTipo]

    readonly_fields = ['productoId']




admin.site.register(ClienteModel)
admin.site.register(ProductoModel, ProductoAdmin)