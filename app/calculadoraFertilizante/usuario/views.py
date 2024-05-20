from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from .forms import UserForm
from django.urls import reverse_lazy

# Importaciones necesarias
# - render: Para renderizar plantillas
# - CreateView, UpdateView, DeleteView: Vistas genéricas de Django para crear, actualizar y eliminar objetos
# - LoginView: Vista de Django para el inicio de sesión de usuarios
# - AuthenticationForm: Formulario de autenticación proporcionado por Django
# - User: Modelo de usuario de Django
# - SuccessMessageMixin: Mezcla de Django para mostrar mensajes de éxito en las vistas basadas en clases
# - UserForm: Formulario personalizado para la creación de usuarios
# - reverse_lazy: Utilidad de Django para la resolución inversa de URLs

# Vistas

# Vista para registrar un nuevo usuario
class RegistrarView(SuccessMessageMixin, CreateView):
    model = User  # Modelo asociado al formulario
    form_class = UserForm  # Clase del formulario a utilizar
    success_url = reverse_lazy('login')  # URL a la que se redirige después del registro exitoso
    success_message = "%(username)s ha sido creada exitosamente."  # Mensaje de éxito que se mostrará al usuario

# Vista para el inicio de sesión de usuarios
class LoginView(LoginView):
    template_name = 'login.html'  # Plantilla HTML para la página de inicio de sesión
    form_class = AuthenticationForm  # Clase del formulario de autenticación a utilizar

