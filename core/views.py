from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import MovimientoForm
from .models import Billetera, Movimiento, Usuario


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('index')
    else:
        form = AuthenticationForm()

    return render(request, 'core/login.html', {'form': form})


@login_required(login_url='login')
def index(request):
    usuario, _ = Usuario.objects.get_or_create(
        auth_user=request.user,
        defaults={
            'nombre': request.user.first_name or request.user.username,
            'apellido': request.user.last_name,
            'correo': request.user.email,
        },
    )
    billetera, _ = Billetera.objects.get_or_create(usuario=usuario)
    movimientos = Movimiento.objects.filter(billetera=billetera)
    saldo = billetera.consultarSaldo()

    if request.method == 'POST':
        form = MovimientoForm(request.POST)
        if form.is_valid():
            monto = form.cleaned_data['monto']
            tipo = request.POST.get('tipo')

            if tipo == Movimiento.RETIRO and monto > saldo:
                messages.error(request, 'No tienes saldo suficiente para retirar esa cantidad.')
            elif tipo == Movimiento.DEPOSITO:
                billetera.depositar(monto)
                messages.success(request, 'Movimiento guardado correctamente.')
            elif tipo == Movimiento.RETIRO:
                billetera.retirar(monto)
                messages.success(request, 'Movimiento guardado correctamente.')
            return redirect('index')
    else:
        form = MovimientoForm()

    return render(request, 'core/index.html', {
        'form': form,
        'saldo': saldo,
        'billetera': billetera,
        'usuario_billetera': usuario,
        'movimientos': movimientos[:5],
    })
