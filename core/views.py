from django.shortcuts import render, redirect
from .forms import NotaForm
from .models import Nota


def index(request):
    """Muestra el formulario y la lista de notas guardadas.

    Si se envía el formulario por POST y es válido, guarda la nota
    en la base de datos SQLite y redirige a la misma página (patrón
    Post/Redirect/Get) para evitar reenvíos duplicados.
    """
    if request.method == 'POST':
        form = NotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = NotaForm()

    notas = Nota.objects.all()

    return render(request, 'core/index.html', {
        'form': form,
        'notas': notas,
    })
