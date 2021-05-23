from django import forms
from modelos.models import Trabajos, Stock, Empleados

trabajos = (('ALISADO', 'Alisado'),
            ('ARGAN', 'Argan'),
            ('BALAYAGE', 'Balayage'),
            ('BARBA', 'Barba'),
            ('BIOMOLECULAR', 'Biomolecular'),
            ('BIOTINA', 'Biotina'),
            ('BOTOX', 'Botox'),
            ('CORTE', 'Corte'),
            ('TINTURA', 'Tintura'),
            ('UÑAS', 'Uñas'),
            ('VENTA', 'Venta')
           )

class TrabajosForm(forms.ModelForm):
    trabajo  = forms.ChoiceField(choices=trabajos, label='', widget=forms.Select(attrs={'class': 'browser-default'}))
    nombre   = forms.CharField(label='Nombre cliente', required=True, widget=forms.TextInput(attrs={'pattern':'^[A-Za-z\s]+$', 'title':'Solo letras'}))
    telefono = forms.IntegerField(label='Telefono cliente', widget=forms.TextInput(attrs={'title':'Solo numeros y sin espacios'}))
    precio   = forms.DecimalField(label='Precio', required=True, widget=forms.TextInput(attrs={'pattern':'^[0-9]+$', 'title':'Solo numeros, hasta 99999'}))
    empleado = forms.ModelChoiceField(queryset=Empleados.objects, label='', empty_label="Empleado", widget=forms.Select(attrs={'class': 'browser-default'}))
    tarjeta  = forms.BooleanField(label='',required=False)

    class Meta:
        model  = Trabajos
        fields = [
            'trabajo',
            'nombre',
            'telefono',
            'precio',
            'empleado',
            'tarjeta'
        ]


class StockForm(forms.ModelForm):
    producto   = forms.ModelChoiceField(queryset=Stock.objects.filter(accion='INGRESO').order_by('producto'), label='', empty_label="Producto", widget=forms.Select(attrs={'class': 'browser-default'}))
    cantidad   = forms.IntegerField(label='Cantidad', required=True, widget=forms.TextInput(attrs={'pattern':'^[0-9]+$', 'title':'Solo numeros'}))

    class Meta:
        model  = Stock
        fields = [
            'producto',
            'cantidad',
        ]