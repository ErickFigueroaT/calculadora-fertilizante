from django.contrib import admin
from .models import TipoCultivo, Cultivo  # Importa los modelos TipoCultivo y Cultivo desde el mismo directorio

# Registra los modelos en el panel de administración de Django
admin.site.register(TipoCultivo)  # Registra el modelo TipoCultivo en el panel de administración
admin.site.register(Cultivo)      # Registra el modelo Cultivo en el panel de administración
