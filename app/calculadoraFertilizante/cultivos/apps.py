from django.apps import AppConfig

# Definición de la configuración de la aplicación 'cultivos'
class CultivosConfig(AppConfig):
    # Define el tipo de campo de clave primaria automática por defecto para los modelos de esta aplicación
    default_auto_field = 'django.db.models.BigAutoField'
    
    # Define el nombre de la aplicación
    name = 'cultivos'

