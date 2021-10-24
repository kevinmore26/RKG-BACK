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
        title = "😼 API de RKG 🐶",
        default_version = "v1",
        description = "Bienvenido a la API de MascotitasRKG 👳‍♂️🧨",
        contact = openapi.Contact(email="kore_2608@hotmail.com"),
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