from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mensajes/', include('chat.urls')),
    path('', include('bienvenida.urls')),
]
