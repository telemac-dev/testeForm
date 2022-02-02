from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from contato.models import Contato
from contato.forms import InserirContatoForm  

# Create your views here.
class ContatoView(TemplateView):
    #template_name = 'html/base.html'
    template_name = 'contato/contato.html'
    

class ContatoCreateView(CreateView):
    model = Contato
    #fields = '__all__'
    template_name = 'contato/contato_create.html'
    form_class = InserirContatoForm
    #success_url = reverse_lazy('')