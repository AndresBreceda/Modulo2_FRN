from django.contrib import admin
from .models import Maestro, Alumno

class MaestroAdmin(admin.ModelAdmin):
    list_display = ['matricula', 'nombre', 'materia', 'email', 'creado_en']

class AlumnoAdmin(admin.ModelAdmin):
    list_display = ['matricula', 'nombre', 'grado', 'email', 'creado_en']

admin.site.register(Maestro, MaestroAdmin)
admin.site.register(Alumno, AlumnoAdmin)