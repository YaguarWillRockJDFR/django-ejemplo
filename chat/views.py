from django.shortcuts import render
from .models import Mensaje

def mostrar_mensajes(request):
    mensajes = Mensaje.objects.all().order_by('id')
    return render(request, 'chat/mensajes.html', {'mensajes': mensajes})
