from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, TemplateView

from contato.forms import ContatoForm
from contato.models import Contato


# Create your views here.
class ContatoView(TemplateView):
    #template_name = 'html/base.html'
    template_name = 'contato/contato.html'


class ContatoListView(ListView):
    model = Contato
    queryset = Contato.objects.all().order_by('nome')
    template_name = 'contato/contato_list.html'


class ContatoCreateView(CreateView):
    model = Contato
    field = '__all__'
    template_name = 'contato/contato_create.html'
    form_class = ContatoForm
    success_url = reverse_lazy('contato-home')
