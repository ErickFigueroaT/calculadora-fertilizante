from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView

# Importaciones necesarias
# - admin: Para las URLs del panel de administración de Django
# - path: Para definir las rutas de URL
# - include: Para incluir URLs de otras aplicaciones
# - views: Módulo que contiene las vistas de la aplicación actual
# - LogoutView: Vista de Django para cerrar sesión de usuarios

urlpatterns = [
    # Rutas de URL
    path('registrar/', views.RegistrarView.as_view(), name='registrar'),  # URL para registrar un nuevo usuario
    path('entrar/', views.LoginView.as_view(), name='login'),  # URL para iniciar sesión de usuario
    path('salir/', LogoutView.as_view(), name='logout'),  # URL para cerrar sesión de usuario
]
