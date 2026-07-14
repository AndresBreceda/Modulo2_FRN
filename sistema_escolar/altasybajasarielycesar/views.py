from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import MaestroForm, AlumnoForm
from .models import Maestro, Alumno


def index(request):
    """Muestra los formularios de alta y las listas de maestros y alumnos.

    Distingue qué formulario se envió por POST usando el campo oculto
    'form_type'. Usa el patrón Post/Redirect/Get para evitar reenvíos
    duplicados al recargar la página.
    """
    maestro_form = MaestroForm(prefix='maestro')
    alumno_form = AlumnoForm(prefix='alumno')

    if request.method == 'POST':
        form_type = request.POST.get('form_type')

        if form_type == 'maestro':
            maestro_form = MaestroForm(request.POST, prefix='maestro')
            if maestro_form.is_valid():
                maestro_form.save()
                messages.success(request, 'Maestro dado de alta correctamente.')
                return redirect('altasybajasarielycesar_index')

        elif form_type == 'alumno':
            alumno_form = AlumnoForm(request.POST, prefix='alumno')
            if alumno_form.is_valid():
                alumno_form.save()
                messages.success(request, 'Alumno dado de alta correctamente.')
                return redirect('altasybajasarielycesar_index')

    maestros = Maestro.objects.all()
    alumnos = Alumno.objects.all()

    return render(request, 'altasybajasarielycesar/index.html', {
        'maestro_form': maestro_form,
        'alumno_form': alumno_form,
        'maestros': maestros,
        'alumnos': alumnos,
    })


def eliminar_maestro(request, pk):
    """Da de baja (elimina) a un maestro por su id."""
    maestro = get_object_or_404(Maestro, pk=pk)
    if request.method == 'POST':
        maestro.delete()
        messages.success(request, 'Maestro dado de baja correctamente.')
    return redirect('altasybajasarielycesar_index')


def eliminar_alumno(request, pk):
    """Da de baja (elimina) a un alumno por su id."""
    alumno = get_object_or_404(Alumno, pk=pk)
    if request.method == 'POST':
        alumno.delete()
        messages.success(request, 'Alumno dado de baja correctamente.')
    return redirect('altasybajasarielycesar_index')
