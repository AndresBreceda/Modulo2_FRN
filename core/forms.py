from django import forms

from .models import Registro


class RegistroForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = ['texto']
        widgets = {
            'texto': forms.TextInput(attrs={'placeholder': 'Escribe algo aqui...'})
        }


class MovimientoForm(forms.Form):
    monto = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        min_value=1,
        widget=forms.NumberInput(attrs={
            'placeholder': '0.00',
            'step': '0.01',
            'min': '1',
        }),
    )
