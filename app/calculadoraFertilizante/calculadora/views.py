from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from cultivos.models import Cultivo
from cultivos.forms import FormCultivo
from django.http import HttpResponse
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle,Paragraph
from io import BytesIO
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Define las vistas para la aplicación de la Calculadora de Fertilizante
"""
Vista para generar un documento PDF con los datos de la calculadora.

Parámetros:
- request: La solicitud HTTP recibida.
- nombre: Nombre del cultivo.
- rendimiento: Rendimiento del cultivo.
- humedad: Porcentaje de humedad del cultivo.
- todo: Lista de tuplas que contiene la información de los nutrientes.

Retorna:
- response: Respuesta HTTP con el PDF generado.
"""
    # Crear contenido del PDF
@login_required

def generar_pdf(request, nombre, rendimiento, humedad, todo, columnas):
    
    # Crear contenido del PDF
    buffer = BytesIO()
    pdf = SimpleDocTemplate(buffer, pagesize=letter)

    # Estilos
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        name='TitleStyle',
        parent=styles['Heading1'],
        alignment=1,  # 0 = left, 1 = center, 2 = right
        fontSize=16,
        textColor=colors.darkblue
    )

    

    if columnas == 3:
        # Título del PDF
        titulo = Paragraph(f"Informe de {nombre}", title_style)
        data = [['Nutriente', 'Absorción (kg ha^-1)', 'Extracción (kg ha^-1)']]
        for nu, ab, ex in todo:
            data.append([nu, ab, ex])
    else:
        titulo = Paragraph(f"Informe de {nombre} con estudio de suelo", title_style)

        data = [['Nutriente', 'Absorción (kg ha^-1)', 'Extracción (kg ha^-1)', 'Absorción con estudio de suelo']]
        for nu, ab, ex, ppm in todo:
            data.append([nu, ab, ex, ppm])

    t = Table(data)
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ])
    t.setStyle(style)

    # Construir PDF
    elementos = [titulo, t]
    pdf.build(elementos)
    buffer.seek(0)

    # Generar respuesta HTTP con el PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="informe.pdf"'
    response.write(buffer.getvalue())
    buffer.close()
    return response

"""
    Vista para la calculadora de fertilizantes.

    Parámetros:
    - request: La solicitud HTTP recibida.

    Retorna:
    - render: Renderiza la plantilla 'calculadora.html' con los datos necesarios.
    """


def calculadora(request):
    
    cultivos = Cultivo.objects.all()
    context = {'object_list': cultivos}

    if request.method == 'POST':
        rendimiento = float(request.POST.get('rendimiento'))
        humedad = float(request.POST.get('humedad'))
        cultivo = Cultivo.objects.get(id=request.POST.get('cultivo_id'))
        nombre, tipo, nutrientes, ics = cultivo.str()  
       
        ppm = []
        columnas = 3
        ppm.append(request.POST.get('ppmN', 0))
        ppm.append(request.POST.get('ppmP', 0))
        ppm.append(request.POST.get('ppmK', 0))
        ppm.append(request.POST.get('ppmCa', 0))
        ppm.append(request.POST.get('ppmMg', 0))
        
        absor = absorcion(rendimiento, humedad, nutrientes)

        extrac = extraccion(absor, ics)
        nutr = nutrientes.keys()

        context['nombre'] = nombre
        context['rendimiento'] = rendimiento
        context['humedad'] = humedad
        
        todo = zip(nutr, absor, extrac)
        print(nombre)
        if ppm[0] != '':
            absppm = ppmCalculo(absor, ppm)
            todo = zip(nutr, absor, extrac, absppm)
            columnas = 4
            context['ppm'] = 1

        context['todo'] = todo
        
        # Redirigir a la vista generar_pdf con los datos calculados
        if 'generar_pdf'  in request.POST:
            return generar_pdf(request, nombre, rendimiento, humedad, todo,columnas)
        
    return render(request, 'calculadora.html', context)

def ppmCalculo(absorcion, ppm):
    ppmcal = []
    for ab, pp in zip(absorcion, ppm):
        # conversion de ppm a kg&ha
        kghaNutriente = int(pp) / 1000
        kghaNutriente *= 10000 
        if ab - kghaNutriente < 0:
            ppmcal.append("El suelo tiene el suficiente nutriente.")
        else:
            ppmcal.append(ab - kghaNutriente)
    ppmcal += absorcion[5:]
    print(ppmcal)
    return ppmcal

"""
    Función para calcular la absorción de nutrientes.

    Parámetros:
    - rendimiento: Rendimiento del cultivo.
    - humedad: Porcentaje de humedad del cultivo.
    - nutrientes: Diccionario que contiene los nutrientes y sus valores.

    Retorna:
    - absorcion: Lista con los valores de absorción calculados.
    """

def absorcion(rendimiento, humedad, nutrientes):
    
    absorcion = []

    for nutriente, valor in nutrientes.items():
        resultado = rendimiento * ((100-humedad)/100) * (valor/1000)
        absorcion.append(round(resultado, 2))

    return absorcion

"""
    Función para calcular la extracción de nutrientes.

    Parámetros:
    - absorcion: Lista con los valores de absorción.
    - ics: Diccionario que contiene los índices de cultivo.

    Retorna:
    - extraccion: Lista con los valores de extracción calculados.
    """

def extraccion(absorcion, ics):
    
    extraccion = []
    valoresIcs = list(ics.values())

    for valAbs, valorIcs in zip(absorcion, valoresIcs):
        extraccion.append(round(valAbs * valorIcs, 2))

    return extraccion

"""
    Vista para mostrar un mensaje de bienvenida al usuario logueado.
    """
class BienvenidaView(LoginRequiredMixin, TemplateView):
    
    template_name = 'bienvenida.html'
