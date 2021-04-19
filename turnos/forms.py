from django import forms
from modelos.models import Turnos, Empleados


class TurnosForm(forms.ModelForm):
    fecha    = forms.DateTimeField(label='Fecha y Hora', required=True)
    cliente  = forms.CharField(label='Nombre cliente', required=True, widget=forms.TextInput(attrs={'pattern':'^[A-Za-z]+$', 'title':'Solo letras'}))
    telefono = forms.IntegerField(label='Telefono cliente',required=False, widget=forms.TextInput(attrs={'pattern':'^[0-9]+$', 'title':'Solo numeros'}))
    empleado = forms.ModelChoiceField(queryset=Empleados.objects, label='', empty_label="Empleado", widget=forms.Select(attrs={'class': 'browser-default'}))

    class Meta:
        model  = Turnos
        fields = [
            'fecha',
            'cliente',
            'telefono',
            'empleado'
        ]
        