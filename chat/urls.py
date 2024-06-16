# chat/urls.py

from django.urls import path
from .views import mensaje_list, mensaje_create, mensaje_update, mensaje_delete

urlpatterns = [
    path('', mensaje_list, name='mensaje_list'),
    path('nuevo/', mensaje_create, name='mensaje_create'),
    path('editar/<int:pk>/', mensaje_update, name='mensaje_update'),
    path('eliminar/<int:pk>/', mensaje_delete, name='mensaje_delete'),
]
