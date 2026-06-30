from django.contrib import admin

from .models import Billetera, Movimiento, Registro, Usuario


@admin.register(Registro)
class RegistroAdmin(admin.ModelAdmin):
    list_display = ('id', 'texto')
    search_fields = ('texto',)


@admin.register(Movimiento)
class MovimientoAdmin(admin.ModelAdmin):
    list_display = ('idMovimiento', 'billetera', 'tipo', 'monto', 'fecha')
    list_filter = ('tipo', 'fecha')
    search_fields = ('billetera__usuario__nombre', 'billetera__usuario__auth_user__username')


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('idUsuario', 'nombre', 'apellido', 'correo', 'numeroControl')
    search_fields = ('nombre', 'apellido', 'correo', 'numeroControl')


@admin.register(Billetera)
class BilleteraAdmin(admin.ModelAdmin):
    list_display = ('idBilletera', 'usuario', 'saldo', 'estado', 'fechaCreacion')
    list_filter = ('estado', 'fechaCreacion')
    search_fields = ('usuario__nombre', 'usuario__auth_user__username')
