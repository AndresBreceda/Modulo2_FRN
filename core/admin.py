from django.contrib import admin
from .models import Nota


@admin.register(Nota)
class NotaAdmin(admin.ModelAdmin):
    list_display = ('id', 'texto', 'creado_en')
    search_fields = ('texto',)
