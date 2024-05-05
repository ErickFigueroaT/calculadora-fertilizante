from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import TipoCultivo, Cultivo
from .forms import FormTipoCultivo, FormCultivo

# Create your views here.

class ListaTipoCultivo(ListView):
    model = TipoCultivo

class NuevoTipoCultivo(CreateView):
    model = TipoCultivo
    # fields = 'all'
    form_class = FormTipoCultivo
    extra_context = {'accion':"Nueva"}
    success_url = reverse_lazy ('lista_tipo_cultivo')

class EditarTipoCultivo(UpdateView):
    model = TipoCultivo
    form_class = FormTipoCultivo
    extra_context = {'accion':"Editar"}
    success_url = reverse_lazy ('lista_tipo_cultivo')

class EliminarTipoCultivo(DeleteView):
    model = TipoCultivo
    #form_class = FormInstituciones
    success_url = reverse_lazy ('lista_tipo_cultivo')

class ListaCultivo(ListView):
    model = Cultivo

class NuevoCultivo(CreateView):
    model = Cultivo
    # fields = 'all'
    form_class = FormCultivo
    extra_context = {'accion':"Nueva"}
    success_url = reverse_lazy ('lista_cultivo')

class EditarCultivo(UpdateView):
    model = Cultivo
    form_class = FormCultivo
    extra_context = {'accion':"Editar"}
    success_url = reverse_lazy ('lista_cultivo')

class EliminarCultivo(DeleteView):
    model = Cultivo
    #form_class = FormInstituciones
    success_url = reverse_lazy ('lista_cultivo')