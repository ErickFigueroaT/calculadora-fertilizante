from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from .forms import UserForm
from django.views.generic import TemplateView
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
from .token import token_activacion
from django.core.mail import EmailMessage
# Vistas
User = get_user_model()

# Vista para registrar un nuevo usuario
class RegistrarView(SuccessMessageMixin, CreateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('login')
    success_message = "%(username)s revisa tu correo electronico."

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()

        sitio = get_current_site(self.request)
        #subject = 'Confirma tu registro en calculadora'
        uid = urlsafe_base64_encode(force_bytes(user.id))
        token = token_activacion.make_token(user) 
        # Imprimir el token generado
        print(f"Token generado: {token}")  

        mensaje = render_to_string('confirm_email.html', {
            'user': user,
            'sitio': sitio,
            'uid': uid,
            'token': token,
        })
        asunto = 'Activar cuenta'
        para = user.email
        email = EmailMessage(
            
            asunto,
            mensaje,
            to=[para],
        )
        email.content_subtype = 'html'
        email.send()
        return super().form_valid(form)



# Vista para el inicio de sesión de usuarios
class LoginView(LoginView):
    template_name = 'login.html'  # Plantilla HTML para la página de inicio de sesión
    form_class = AuthenticationForm  # Clase del formulario de autenticación a utilizar

class ConfirmarRegistro(TemplateView):
    def get(self,request,*args,**kwargs):
        try:
            uid = urlsafe_base64_decode(kwargs['uidb64'])
            token =(kwargs['token'])
            user = User.objects.get(pk=uid)
        except(TypeError,ValueError,User.DoesNotExist):
            user = None
        if (user is not None and  token_activacion.check_token(user,token)):
            user.is_active = True
            user.save()
            messages.success(request,'Cuenta activada, ingresar datos')
        else:
             messages.error(request,'Token invalido, contacta al administrador')
        return redirect('login')

