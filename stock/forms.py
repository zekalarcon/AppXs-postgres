from django import forms
from modelos.models import Stock

class AgregarStockForm(forms.ModelForm):
    producto   = forms.CharField(label='Producto', required=True, widget=forms.TextInput(attrs={'pattern':'^[a-zA-Z0-9.]+*$', 'title':'Solo letras, numeros y .'}))
    cantidad   = forms.IntegerField(label='Cantidad', required=True, widget=forms.TextInput(attrs={'pattern':'^[0-9]+$', 'title':'Solo numeros'}))

    class Meta:
        model  = Stock
        fields = [
            'producto',
            'cantidad',
        ]


class ConsultaStockForm(forms.ModelForm):
    producto_consulta   = forms.CharField(label='Nombre producto', required=True, widget=forms.TextInput(attrs={'pattern':'^[a-zA-Z0-9.]+*$', 'title':'Solo letras, numeros y .' }))

    class Meta:
        model  = Stock
        fields = [
            'producto_consulta',
        ]