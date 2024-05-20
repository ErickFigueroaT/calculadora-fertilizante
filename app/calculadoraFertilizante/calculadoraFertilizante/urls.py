from django.contrib import admin
from django.urls import path, include
from calculadora.views import BienvenidaView  # Importa la vista BienvenidaView desde la aplicación calculadora

urlpatterns = [
    # Ruta para acceder al panel de administración
    path('admin/', admin.site.urls),

    # Rutas para las funcionalidades de la calculadora
    path('calculadora/', include ('calculadora.urls')),

    # Rutas para las funcionalidades de usuario
    path('usuario/', include ('usuario.urls')),

    # Rutas para las funcionalidades relacionadas con los cultivos
    path('cultivos/', include('cultivos.urls')),

    # Ruta principal, muestra la vista BienvenidaView
    path('', BienvenidaView.as_view(), name='bienvenida'),
]
