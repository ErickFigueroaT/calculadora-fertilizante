from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import TipoCultivo, Cultivo
from .forms import FormTipoCultivo, FormCultivo
from django.contrib.auth.mixins import PermissionRequiredMixin


# Vista basada en clase que muestra una lista de tipos de cultivo
class ListaTipoCultivo(ListView):
    model = TipoCultivo

# Vista basada en clase para crear un nuevo tipo de cultivo
class NuevoTipoCultivo(LoginRequiredMixin, CreateView):
    model = TipoCultivo
    form_class = FormTipoCultivo
    extra_context = {'accion': "Nuevo"}
    success_url = reverse_lazy('lista_tipo_cultivo')

# Vista basada en clase para editar un tipo de cultivo existente
class EditarTipoCultivo(LoginRequiredMixin, UpdateView):
    model = TipoCultivo
    form_class = FormTipoCultivo
    extra_context = {'accion': "Editar"}
    success_url = reverse_lazy('lista_tipo_cultivo')

# Vista basada en clase para eliminar un tipo de cultivo existente
class EliminarTipoCultivo(LoginRequiredMixin, DeleteView):
    model = TipoCultivo
    success_url = reverse_lazy('lista_tipo_cultivo')

# Vista basada en clase que muestra una lista de cultivos
class ListaCultivo(LoginRequiredMixin, ListView):
    model = Cultivo

# Vista basada en clase para crear un nuevo cultivo
class NuevoCultivo(LoginRequiredMixin, CreateView):
    model = Cultivo
    form_class = FormCultivo
    extra_context = {'accion': "Nuevo"}
    success_url = reverse_lazy('lista_cultivo')

# Vista basada en clase para editar un cultivo existente
class EditarCultivo(LoginRequiredMixin, UpdateView):
    model = Cultivo
    form_class = FormCultivo
    extra_context = {'accion': "Editar"}
    success_url = reverse_lazy('lista_cultivo')

# Vista basada en clase para eliminar un cultivo existente
class EliminarCultivo(LoginRequiredMixin, DeleteView):
    model = Cultivo
    success_url = reverse_lazy('lista_cultivo')
