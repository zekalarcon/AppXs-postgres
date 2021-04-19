from django import forms
from modelos.models import Trabajos

class ClienteForm(forms.ModelForm):
    nombre   = forms.CharField(label='Cliente', required=True, widget=forms.TextInput(attrs={'pattern':'^[A-Za-z]+$', 'title':'Solo letras'}))

    class Meta:
        model  = Trabajos
        fields = [
            'nombre',
        ]
