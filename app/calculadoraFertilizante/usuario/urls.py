from django.contrib import admin
from django.urls import path,include
from . import views
from django. contrib.auth.views import LogoutView
urlpatterns = [
    path('registrar/', views.RegistrarView.as_view(), name='registrar' ),
    path('entrar/', views.LoginView.as_view(), name='login'),
    path('salir',LogoutView.as_view(),name='logout'),
]