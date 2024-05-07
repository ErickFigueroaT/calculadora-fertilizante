from django.shortcuts import render
from django.views.generic import  TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def calculadora(request):
    return render(request, 'calculadora.html')

class BienvenidaView(LoginRequiredMixin,TemplateView):
    template_name = 'bienvenida.html'
