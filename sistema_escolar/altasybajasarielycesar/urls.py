from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='altasybajasarielycesar_index'),
    path('maestros/<int:pk>/eliminar/', views.eliminar_maestro, name='altasybajasarielycesar_eliminar_maestro'),
    path('alumnos/<int:pk>/eliminar/', views.eliminar_alumno, name='altasybajasarielycesar_eliminar_alumno'),
]
