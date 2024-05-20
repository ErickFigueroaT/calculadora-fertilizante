from django.apps import AppConfig

# Clase de configuración de la aplicación "usuario"
class UsuarioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # Configuración predeterminada para el campo de clave primaria automático
    name = 'usuario'  # Nombre de la aplicación

