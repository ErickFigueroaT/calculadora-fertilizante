from django.shortcuts import render
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from .forms import UserForm
from django.urls import reverse_lazy

# Create your views here.

class RegistrarView(SuccessMessageMixin, CreateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('login')
    success_message = "%(username)s ha sido creada exitosamente."

class LoginView(LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm
