from django.db import models

class Maestro(models.Model):
    matricula = models.CharField(max_length=20, unique=True, null=True, blank=True)
    nombre = models.CharField(max_length=100)
    materia = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    creado_en = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.nombre

class Alumno(models.Model):
    matricula = models.CharField(max_length=20, unique=True, null=True, blank=True)
    nombre = models.CharField(max_length=100)
    grado = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)
    creado_en = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.nombre