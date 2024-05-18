from django.shortcuts import render
from django.views.generic import  TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from cultivos.models import Cultivo
# Create your views here.
def calculadora(request):
    cultivos = Cultivo.objects.all()
    resultado = 10
    context = {
        'object_list': cultivos,
        'resultado': resultado
    }
    return render(request, 'calculadora.html',context)

class BienvenidaView(LoginRequiredMixin,TemplateView):
    template_name = 'bienvenida.html'
