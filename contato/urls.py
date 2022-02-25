from django.urls import path
from django.views.generic import TemplateView

from contato.views import ContatoView, ContatoListView, ContatoCreateView, ContatoUpdateView, ContatoDeleteView


urlpatterns = [
    path('', ContatoView.as_view(), name='contato-home'),
    path('lista/', ContatoListView.as_view(), name='contato-lista'),
    path('novo/', ContatoCreateView.as_view(), name='contato-novo'),
    path('editar/<int:pk>', ContatoUpdateView.as_view(), name='contato-edita'),
    path('remover/<int:pk>', ContatoDeleteView.as_view(), name='contato-remover'),
]