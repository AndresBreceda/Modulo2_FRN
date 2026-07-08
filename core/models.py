from django.db import models


class Nota(models.Model):
    """Modelo simple que guarda un texto ingresado por el usuario."""
    texto = models.CharField(max_length=200)
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-creado_en']

    def __str__(self):
        return self.texto
