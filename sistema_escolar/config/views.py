from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from alumnos_maestros.models import Alumno, Maestro, Materia, Inscripcion

@login_required
def home(request):

    modulos = [
        {
            "nombre": "Alumnos y Maestros",
            "descripcion": "Administración de alumnos, maestros, materias e inscripciones.",
            "url": "dashboard",
            "icono": "bi-mortarboard-fill",
        },
        {
            "nombre": "Calificaciones",
            "descripcion": "Registro y consulta de calificaciones.",
            "url": "calificaciones_dashboard",
            "icono": "bi-journal-check",
        },
        {
            "nombre": "Horarios",
            "descripcion": "Administración de horarios.",
            "url": "horarios_index",
            "icono": "bi-calendar-week",
        },
        {
            "nombre": "Empresas",
            "descripcion": "Empresas vinculadas.",
            "url": "empresa_list",
            "icono": "bi-buildings-fill",
        },
        {
            "nombre": "Billetera",
            "descripcion": "Ingresos y egresos.",
            "url": "billetera_list",
            "icono": "bi-wallet2",
        },
    ]

    context = {
        "modulos": modulos,
        "total_alumnos": Alumno.objects.filter(activo=True).count(),
        "total_maestros": Maestro.objects.filter(activo=True).count(),
        "total_materias": Materia.objects.filter(activa=True).count(),
        "total_inscripciones": Inscripcion.objects.filter(activo=True).count(),
        "alumnos_recientes": Alumno.objects.filter(activo=True).order_by("-id")[:5],
    }

    return render(request, "home.html", context)