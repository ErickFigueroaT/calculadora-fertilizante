from django.apps import AppConfig

class CalculadoraConfig(AppConfig):
    """
    Clase de configuración de la aplicación Calculadora.

    Esta clase define la configuración de la aplicación Calculadora,
    incluyendo la configuración del campo de auto-incremento predeterminado
    y el nombre de la aplicación.

    Atributos:
    - default_auto_field: Define el tipo de campo de auto-incremento predeterminado
      para los modelos de la aplicación. En este caso, se utiliza un BigAutoField.
    - name: Nombre de la aplicación, que coincide con el nombre del módulo.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'calculadora'

