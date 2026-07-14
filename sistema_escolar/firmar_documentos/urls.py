from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='firmar_documentos_dashboard'),
    path('documentos/', views.documentos, name='firmar_documentos_documentos'),
    path('usuario/', views.usuario, name='firmar_documentos_usuario'),
    path('firma/', views.firma, name='firmar_documentos_firma'),
]
