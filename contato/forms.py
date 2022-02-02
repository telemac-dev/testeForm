from django import forms
from django.forms import ModelForm
from .models import Contato


class InserirContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        widgets = {'tipo_contato' : forms.RadioSelect,}
        fields=('tipo_contato',)