from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import TipoCultivo, Cultivo
from .forms import FormTipoCultivo, FormCultivo

class ListaTipoCultivo(LoginRequiredMixin,ListView):
    model = TipoCultivo

class NuevoTipoCultivo(LoginRequiredMixin,CreateView):
    model = TipoCultivo
    # fields = 'all'
    form_class = FormTipoCultivo
    extra_context = {'accion':"Nuevo"}
    success_url = reverse_lazy ('lista_tipo_cultivo')

class EditarTipoCultivo(LoginRequiredMixin,UpdateView):
    model = TipoCultivo
    form_class = FormTipoCultivo
    extra_context = {'accion':"Editar"}
    success_url = reverse_lazy ('lista_tipo_cultivo')

class EliminarTipoCultivo(LoginRequiredMixin,DeleteView):
    model = TipoCultivo
    #form_class = FormInstituciones
    success_url = reverse_lazy ('lista_tipo_cultivo')

class ListaCultivo(LoginRequiredMixin,ListView):
    model = Cultivo

class NuevoCultivo(LoginRequiredMixin,CreateView):
    model = Cultivo
    # fields = 'all'
    form_class = FormCultivo
    extra_context = {'accion':"Nuevo"}
    success_url = reverse_lazy ('lista_cultivo')

class EditarCultivo(LoginRequiredMixin,UpdateView):
    model = Cultivo
    form_class = FormCultivo
    extra_context = {'accion':"Editar"}
    success_url = reverse_lazy ('lista_cultivo')

class EliminarCultivo(LoginRequiredMixin,DeleteView):
    model = Cultivo
    #form_class = FormInstituciones
    success_url = reverse_lazy ('lista_cultivo')