from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Row, Column, Submit, Button, Div
from crispy_forms.bootstrap import InlineRadios
from django.forms import ModelForm
from .models import Contato


class InserirContatoForm(forms.ModelForm):
    tipo_contato = forms.ChoiceField(choices=[
            ('PF', 'Particular'),
            ('PJ', 'Empresa')],
                                        widget = forms.RadioSelect,
                                        initial='PJ')

    class Meta:
        model = Contato
        fields=('tipo_contato', 'nome', 'cep', 'logradouro', 'email')

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
        #self.fields['cep'].widget.attrs.update(style='max-width: 6em')

        self.fields['tipo_contato'].label = False
        self.fields['nome'].label = False
        # self.helper.form_class = 'form-horizontal'
        # self.helper.label_class = 'col-lg-2'
        # self.helper.field_class = 'col-lg-8'

        self.helper.layout = Layout(
            Row(
                InlineRadios('tipo_contato', css_class='mb-3'),
                ),
            Row(
                Column(
                    Field('nome', css_class="form-control form-control-lg col-md-3")
                    ),
                # Column(
                #     Field('email', css_class="form-control form-control-sm"),
                #     ),
                    css_class="form-horizontal" 
                ),
            Row(
                Column(
                    Field('cep', style='max-width: 6em', css_class='form-control-sm col-md-1' )
                    ),
                ),
            Row(
                Column(
                    Field('logradouro', css_class='form-control-sm col-md-3')
                    ),


                ),
                Submit('submit', 'Salvar', css_class='btn-primary'),
                Button('cancel', 'Cancelar')
            )

#  cep = models.CharField(max_length=8, blank=True, null=True)
#     logradouro = models.CharField(max_length=50)
#     numero = models.CharField(max_length=5)
#     complemento = models.CharField(max_length=50)
#     bairro = models.CharField(max_length=50)
#     cidade = models.CharField(max_length=60)
#     uf = models.CharField(max_l
