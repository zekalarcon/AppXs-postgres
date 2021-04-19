from django import forms
from modelos.models import Empleados, Trabajos

class EmpleadosForm(forms.ModelForm):
    nombre    = forms.CharField(label='Nombre empleado', required=True, widget=forms.TextInput(attrs={'pattern':'^[A-Za-z]+$', 'title':'Solo letras'}))
    telefono  = forms.IntegerField(label='Telefono empleado', widget=forms.TextInput(attrs={'pattern':'^[0-9]+$', 'title':'Solo numeros'}))
    direccion = forms.CharField(label='Direccion empleado', required=True, widget=forms.TextInput(attrs={'pattern':'^[a-zA-Z0-9]+*$', 'title':'Solo letras y numeros'}))
    
    class Meta:
        model  = Empleados
        fields = [
            'nombre',
            'telefono',
            'direccion'
        ]


class EmpleadosInfoForm(forms.ModelForm):
    fecha_inicio    = forms.DateField(label='Fecha Inicial', required=True)
    fecha_fin       = forms.DateField(label='Fecha Final', required=True)
    nombre_consulta = forms.ModelChoiceField(queryset=Empleados.objects, label='', empty_label="Empleado", widget=forms.Select(attrs={'class': 'browser-default'}))

    class Meta:
        model  = Trabajos
        fields = [
            'fecha_inicio',
            'fecha_fin',
            'nombre_consulta' 
        ]