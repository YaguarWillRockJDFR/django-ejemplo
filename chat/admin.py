# chat/admin.py

from django.contrib import admin
from .models import Carrera, Persona, Mensaje

@admin.register(Carrera)
class CarreraAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'status')

@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ap_pat', 'ap_mat', 'usu', 'carrera', 'status')
    search_fields = ('nombre', 'ap_pat', 'ap_mat', 'usu')
    list_filter = ('carrera', 'status')

@admin.register(Mensaje)
class MensajeAdmin(admin.ModelAdmin):
    list_display = ('txt_mensaje', 'persona', 'status')
    search_fields = ('txt_mensaje', 'persona__nombre')
    list_filter = ('status',)
