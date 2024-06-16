# chat/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Mensaje
from .forms import MensajeForm

def mensaje_list(request):
    mensajes = Mensaje.objects.all().order_by('persona__nombre')
    return render(request, 'chat/mensaje_list.html', {'mensajes': mensajes})

def mensaje_create(request):
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mensaje_list')
    else:
        form = MensajeForm()
    return render(request, 'chat/mensaje_form.html', {'form': form})

def mensaje_update(request, pk):
    mensaje = get_object_or_404(Mensaje, pk=pk)
    if request.method == 'POST':
        form = MensajeForm(request.POST, instance=mensaje)
        if form.is_valid():
            form.save()
            return redirect('mensaje_list')
    else:
        form = MensajeForm(instance=mensaje)
    return render(request, 'chat/mensaje_form.html', {'form': form})

def mensaje_delete(request, pk):
    mensaje = get_object_or_404(Mensaje, pk=pk)
    if request.method == 'POST':
        mensaje.delete()
        return redirect('mensaje_list')
    return render(request, 'chat/mensaje_confirm_delete.html', {'mensaje': mensaje})
