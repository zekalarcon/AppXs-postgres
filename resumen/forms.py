from django import forms
from modelos.models import Trabajos

class ResumenForm(forms.ModelForm):
    fecha_inicio = forms.DateField(label='Fecha Inicial', required=True)
    fecha_fin = forms.DateField(label='Fecha Final', required=True)

    class Meta:
        model  = Trabajos
        fields = [
            'fecha_inicio',
            'fecha_fin'
        ]