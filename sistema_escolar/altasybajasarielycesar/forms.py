from django import forms
from .models import Maestro, Alumno

class MaestroForm(forms.ModelForm):
    class Meta:
        model = Maestro
        fields = ['matricula', 'nombre', 'materia', 'email'] 
        widgets = {
            'matricula': forms.TextInput(attrs={'placeholder': 'Matrícula del maestro'}),
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre del maestro'}),
            'materia': forms.TextInput(attrs={'placeholder': 'Materia que imparte'}),
            'email': forms.EmailInput(attrs={'placeholder': 'correo@ejemplo.com'}),
        }

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['matricula', 'nombre', 'grado', 'email']
        widgets = {
            'matricula': forms.TextInput(attrs={'placeholder': 'Matrícula del alumno'}),
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre del alumno'}),
            'grado': forms.TextInput(attrs={'placeholder': 'Grado / grupo'}),
            'email': forms.EmailInput(attrs={'placeholder': 'correo@ejemplo.com'}),
        }