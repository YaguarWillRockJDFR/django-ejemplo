# chat/models.py

from django.db import models

class Carrera(models.Model):
    nombre = models.CharField(max_length=80)
    status = models.SmallIntegerField()

    def __str__(self):
        return self.nombre

class Persona(models.Model):
    nombre = models.CharField(max_length=80)
    ap_pat = models.CharField(max_length=80)
    ap_mat = models.CharField(max_length=80)
    usu = models.CharField(max_length=80)
    pass_field = models.CharField(max_length=80, default='default_password')  # Añadir un valor predeterminado aquí
    fecha_nac = models.DateField()
    carrera = models.ForeignKey(Carrera, on_delete=models.PROTECT)
    status = models.SmallIntegerField()

    def __str__(self):
        return f"{self.nombre} {self.ap_pat} {self.ap_mat}"

class Mensaje(models.Model):
    txt_mensaje = models.TextField()
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    status = models.SmallIntegerField()

    def __str__(self):
        return f"{self.persona.nombre} - {self.txt_mensaje[:30]}"
