from django.shortcuts import render
from django.views.generic.edit import CreateView
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
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.contrib import messages
# Vistas
User = get_user_model()

# Vista para registrar un nuevo usuario
class RegistrarView(SuccessMessageMixin, CreateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('login')
    success_message = "%(username)s ha sido creada exitosamente."

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()

        current_site = get_current_site(self.request)
        subject = 'Confirma tu registro en MiSitio'
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)

        # Imprimir el token generado
        print(f"Token generado: {token}")  

        message = render_to_string('confirm_email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': uid,
            'token': token,
        })
        user.email_user(subject, message)

        return super().form_valid(form)



# Vista para el inicio de sesión de usuarios
class LoginView(LoginView):
    template_name = 'login.html'  # Plantilla HTML para la página de inicio de sesión
    form_class = AuthenticationForm  # Clase del formulario de autenticación a utilizar

def confirmar_registro(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
        print(f"Decoded UID: {uid}")  # Depuración
        print(f"User found: {user}")  # Depuración
        print(f"User attributes at token validation: {user.__dict__}")  # Depuración detallada de atributos del usuario
    except (TypeError, ValueError, OverflowError, User.DoesNotExist) as e:
        user = None
        print(f"Error decoding uid or fetching user: {e}")

    if user is not None:
        valid_token = default_token_generator.check_token(user, token)
        print(f"Token valid: {valid_token}")  # Depuración
        if valid_token:
            user.is_active = True
            user.save()
            messages.success(request, 'Tu registro ha sido confirmado. Ahora puedes iniciar sesión.')
        else:
            messages.error(request, 'El enlace de confirmación es inválido o ha expirado.')
            print(f"Token invalid for user: {user}")  # Depuración
            print(f"Provided token: {token}")  # Depuración
            print(f"Expected token: {default_token_generator.make_token(user)}")  # Generar token esperado para comparación
    else:
        messages.error(request, 'El enlace de confirmación es inválido o ha expirado.')
        print("User is None")  # Depuración

    return redirect('login')

