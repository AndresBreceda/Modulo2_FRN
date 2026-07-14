import hashlib

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .models import Documento, Firma


def _hash_bloque(payload, hash_anterior):
    return hashlib.sha256(f"{hash_anterior}{payload}".encode()).hexdigest()


@login_required
def dashboard(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo', '').strip()
        contenido = request.POST.get('contenido', '').strip()

        if titulo:
            hash_documento = hashlib.sha256(f"{titulo}{contenido}".encode()).hexdigest()
            documento = Documento.objects.create(
                titulo=titulo,
                contenido=contenido,
                usuario=request.user,
                estado='firmado',
                hash_documento=hash_documento,
            )

            ultima_firma = Firma.objects.order_by('-id').first()
            hash_anterior = ultima_firma.hash_bloque if ultima_firma else '0'
            payload = f"Type: documento_firmado | Title: {titulo} | DocHash: {hash_documento}"

            Firma.objects.create(
                documento=documento,
                usuario=request.user,
                hash_anterior=hash_anterior,
                hash_bloque=_hash_bloque(payload, hash_anterior),
                payload=payload,
            )

        return redirect('firmar_documentos_dashboard')

    return render(request, 'firmar_documentos/dashboard.html', {
        'total_bloques': Firma.objects.count(),
        'documentos_firmados': Documento.objects.filter(estado='firmado').count(),
    })


@login_required
def documentos(request):
    return render(request, 'firmar_documentos/documentos.html', {
        'documentos': Documento.objects.select_related('usuario').order_by('-fecha_creacion'),
    })


@login_required
def usuario(request):
    return render(request, 'firmar_documentos/usuario.html')


@login_required
def firma(request):
    return render(request, 'firmar_documentos/firma.html', {
        'firmas': Firma.objects.select_related('documento').order_by('id'),
    })
