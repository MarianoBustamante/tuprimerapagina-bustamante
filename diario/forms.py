from django import forms
from .models import Escritor, Tema, Entrada

class EscritorForm(forms.ModelForm):
    class Meta:
        model = Escritor
        fields = '__all__'

class TemaForm(forms.ModelForm):
    class Meta:
        model = Tema
        fields = '__all__'

class EntradaForm(forms.ModelForm):
    class Meta:
        model = Entrada
        fields = '__all__'

class BuscarEntradaForm(forms.Form):
    titulo = forms.CharField(max_length=200, required=False)
