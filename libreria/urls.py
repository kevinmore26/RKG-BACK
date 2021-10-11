from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gestion/', include('gestion.urls')),
    path('facturacion/', include('facturacion.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)