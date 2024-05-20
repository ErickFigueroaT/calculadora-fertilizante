#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
# Comentario explicando el propósito del script

import os
import sys

# Importaciones necesarias
# - os: Módulo para interactuar con el sistema operativo
# - sys: Módulo para proporcionar acceso a algunas variables utilizadas o mantenidas por el intérprete

def main():
    """Run administrative tasks."""
    # Función principal del script

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'calculadoraFertilizante.settings')
    # Configura la variable de entorno 'DJANGO_SETTINGS_MODULE' para usar el archivo de configuración de Django

    try:
        from django.core.management import execute_from_command_line
        # Intenta importar la función execute_from_command_line del módulo de gestión de Django
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
        # Captura la excepción si Django no se puede importar y proporciona instrucciones sobre cómo resolver el problema

    execute_from_command_line(sys.argv)
    # Ejecuta comandos desde la línea de comandos utilizando los argumentos pasados al script

if __name__ == '__main__':
    main()
    # Ejecuta la función main() si el script se ejecuta directamente
