from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Row, Column, Submit
from crispy_forms.bootstrap import InlineRadios
from django.forms import ModelForm
from .models import Contato


class InserirContatoForm(forms.ModelForm):
    tipo_contato = forms.ChoiceField(choices=[
            ('PF', 'Pessoa Fisica'), 
            ('PJ', 'Pessoa Juridica')], 
                                        widget = forms.RadioSelect, 
                                        initial='PJ')
    
    class Meta:
        model = Contato
        fields=('tipo_contato', 'nome', 'email')
        
        widgets = {'nome': forms.TextInput(attrs={'size': '50'}),
                   }
        

    def __init__(self, *args, **kwargs):
        """
        Surcharge de l'initialisation du formulaire
        """
        super().__init__(*args, **kwargs)
        # Tu utilises FormHelper pour customiser ton formulaire
        self.helper = FormHelper()
        # Tu définis l'id et la classe bootstrap de ton formulaire
        
        #self.fields['nome'].widget.attrs.update(style='max-width: 50em')
        #self.fields['email'].widget.attrs.update(style='max-width: 50em')

        self.fields['tipo_contato'].label = False
        
        self.helper.layout = Layout(
            Row(
                InlineRadios('tipo_contato', css_class='mb-3'),
                ),
            Row(
                Column('nome'),
                Column('email'),
                css_class = 'form-horizontal'
                ),
                Submit('submit', 'Salvar', css_class='btn-primary'),
            )

        