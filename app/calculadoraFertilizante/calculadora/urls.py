
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    # Ruta para la calculadora de fertilizantes
    path('calcula/', views.calculadora, name='calculadora'),
]
