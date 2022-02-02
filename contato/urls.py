from django.urls import path
from django.views.generic import TemplateView

from contato.views import ContatoView, ContatoCreateView


urlpatterns = [
    path('', ContatoView.as_view(), name='contato-home'),
    path('novo/', ContatoCreateView.as_view(), name='contato-novo'),
]