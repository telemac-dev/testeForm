from ast import Delete

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, ListView,
                                  TemplateView, UpdateView)

from contato.forms import ContatoForm
from contato.models import Contato


# Create your views here.
class ContatoView(TemplateView):
    #template_name = 'html/base.html'
    template_name = 'contato/contato.html'


class ContatoListView(ListView):
    model = Contato
    # queryset = Contato.objects.all().order_by('nome')
    template_name = 'contato/contato_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        filtro_nome = self.request.GET.get('nome') or None
        filtro_tipo_contato = self.request.GET.get('tipo_contato') or None

        if filtro_nome:
            queryset = queryset.filter(nome__contains=filtro_nome)
        if filtro_tipo_contato == 'PF':
            queryset = queryset.filter(tipo_contato='PF')
        elif filtro_tipo_contato == 'PJ':
            queryset = queryset.filter(tipo_contato='PJ')
        else:
            queryset = queryset.filter()

        return queryset


class ContatoCreateView(CreateView):
    model = Contato
    field = '__all__'
    template_name = 'contato/contato_create.html'
    form_class = ContatoForm
    success_url = reverse_lazy('contato-lista')


class ContatoUpdateView(UpdateView):
    model = Contato
    field = '__all__'
    template_name = 'contato/contato_create.html'
    form_class = ContatoForm
    success_url = reverse_lazy('contato-lista')


class ContatoDeleteView(DeleteView):
    model = Contato
    success_url = reverse_lazy('contato-lista')
