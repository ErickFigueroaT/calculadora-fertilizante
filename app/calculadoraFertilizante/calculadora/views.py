from django.shortcuts import render
from django.views.generic import  TemplateView
# Create your views here.
def calculadora(request):
    return render(request, 'calculadora.html')

class BienvenidaView(TemplateView):
    template_name = 'bienvenida.html'
