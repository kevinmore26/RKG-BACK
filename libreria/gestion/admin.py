from django.contrib import admin
from .models import ClienteModel, ProductoModel,AdopcionModel

class ProductoAdmin(admin.ModelAdmin):
    # modificar la vista del modelo
    # no funciona de la misma manera que el ordenamiento (cuando es - significa desc)
    list_display = ['productoId', 'productoNombre', 'productoPrecio']
    # agregar un buscador para hacer busquedas
    search_fields = ['productoNombre', 'productoUnidadMedida']
    # crea un campo de busqueda de acceso rapido
    list_filter = ['productoUnidadMedida']
    # indico si se desea ver algun campo que el usuario no puede manipular
    readonly_fields = ['productoId']


class AdopcionesAdmin(admin.ModelAdmin):
    list_display = ['adopcionId', 'adopcionNombre', 'adopcionEdad',]
    search_fields = ['adopcionNombre', 'adopcionTamaño']
    list_filter = ['adopcionTamaño']
    readonly_fields = ['productoId']


admin.site.register(ClienteModel)
admin.site.register(ProductoModel, ProductoAdmin)
admin.site.register(AdopcionModel)

