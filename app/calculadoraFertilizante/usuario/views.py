from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from .forms import UserForm
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.contrib import messages

# Vistas
User = get_user_model()

# Vista para registrar un nuevo usuario
class RegistrarView(SuccessMessageMixin, CreateView):
    model = User  # Modelo asociado al formulario
    form_class = UserForm  # Clase del formulario a utilizar
    success_url = reverse_lazy('login')  # URL a la que se redirige después del registro exitoso
    success_message = "%(username)s ha sido creada exitosamente."  # Mensaje de éxito que se mostrará al usuario
    
    def form_valid(self, form):
        # Guardar el usuario sin commit para poder modificarlo antes de guardarlo definitivamente
        user = form.save(commit=False)
        user.is_active = False  # El usuario no será activo hasta que confirme su correo electrónico
        user.save()
        
        # Enviar correo electrónico de confirmación
        current_site = get_current_site(self.request)
        subject = 'Confirma tu registro en MiSitio'
        message = render_to_string('confirm_email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': default_token_generator.make_token(user),
        })
        user.email_user(subject, message)

        return super().form_valid(form)

# Vista para el inicio de sesión de usuarios
class LoginView(LoginView):
    template_name = 'login.html'  # Plantilla HTML para la página de inicio de sesión
    form_class = AuthenticationForm  # Clase del formulario de autenticación a utilizar

def confirmar_registro(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Tu registro ha sido confirmado. Ahora puedes iniciar sesión.')
    else:
        messages.error(request, 'El enlace de confirmación es inválido o ha expirado.')

    return redirect('login')