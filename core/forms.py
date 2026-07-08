from django import forms
from .models import Nota


class NotaForm(forms.ModelForm):
    """ModelForm para crear/editar una Nota."""

    class Meta:
        model = Nota
        fields = ['texto']
        widgets = {
            'texto': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Escribe algo aquí...',
                'maxlength': 200,
            }),
        }
        labels = {
            'texto': 'Texto',
        }
