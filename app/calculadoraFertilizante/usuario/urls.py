from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('registrar/', views.RegistrarView.as_view(), name='registrar' ),
    path('entrar/', views.LoginView.as_view(), name='login')
]