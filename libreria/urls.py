from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
schema_view = get_schema_view(
    openapi.Info(
        title = "API de gestion de minimarket",
        default_version = "v1",
        description = "API usando DRF para el manejo de un minimarket con varios almacenes",
        terms_of_service = "https://www.google.com",
        contact = openapi.Contact(email="ederiveroman@gmail.com"),
        # https://es.wikipedia.org/wiki/Licencia_de_software
        license = openapi.License(name="MIT", url="https://es.wikipedia.org/wiki/Licencia_MIT")
    ),
    public = True,
    permission_classes = ( permissions.AllowAny, ),
)



   
urlpatterns = [
    path('',schema_view.with_ui('swagger', cache_timeout=0)),
    # path('admin/', admin.site.urls),
    path('gestion/', include('gestion.urls')),
    path('facturacion/', include('facturacion.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)