from django.shortcuts import render
from django.views.generic import  TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from cultivos.models import Cultivo
from cultivos.forms import FormCultivo
from django.http import HttpResponse
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from io import BytesIO

# Create your views here.

def generar_pdf(request, nombre, rendimiento, humedad, todo):
    # Crear contenido del PDF
    buffer = BytesIO()
    pdf = SimpleDocTemplate(buffer, pagesize=letter)
    data = [['Nutriente', 'Absorción (kg ha^-1)', 'Extracción (kg ha^-1)']]
    for nu, ab, ex in todo:
        data.append([nu, ab, ex])
    t = Table(data)
    style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                        ('GRID', (0, 0), (-1, -1), 1, colors.black)])
    t.setStyle(style)

    # Construir PDF
    elementos = [t]
    pdf.build(elementos)
    buffer.seek(0)

    # Generar respuesta HTTP con el PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="informe.pdf"'
    response.write(buffer.getvalue())
    buffer.close()
    return response
    
def calculadora(request):
    cultivos = Cultivo.objects.all()
    context = {'object_list': cultivos}

    if request.method == 'POST':
        rendimiento = float(request.POST.get('rendimiento'))
        humedad = float(request.POST.get('humedad'))
        cultivo = Cultivo.objects.get(id=request.POST.get('cultivo_id'))
        nombre, tipo, nutrientes, ics = cultivo.str()  

        absor = absorcion(rendimiento, humedad, nutrientes)
        extrac = extraccion(absor, ics)
        nutr = nutrientes.keys()

        context['nombre'] = nombre
        context['rendimiento'] = rendimiento
        context['humedad'] = humedad
        
        todo = zip(nutr, absor, extrac)
        context['todo'] = todo

        # Redirigir a la vista generar_pdf con los datos calculados
        pdf = generar_pdf(request, nombre, rendimiento, humedad, todo)

        if 'generar_pdf' in request.POST:
            return pdf 
            
    return render(request, 'calculadora.html', context)


def absorcion(rendimiento, humedad, nutrientes):
    absorcion = []

    for nutriente, valor in nutrientes.items():
        resultado = rendimiento * ((100-humedad)/100) * (valor/1000)
        absorcion.append(round(resultado, 2))

    return absorcion

def extraccion(absorcion, ics):
    extraccion = []
    valoresIcs = list(ics.values())

    for valAbs, valorIcs in zip(absorcion, valoresIcs):
        extraccion.append(round(valAbs * valorIcs, 2))

    return extraccion

class BienvenidaView(LoginRequiredMixin,TemplateView):
    template_name = 'bienvenida.html'
