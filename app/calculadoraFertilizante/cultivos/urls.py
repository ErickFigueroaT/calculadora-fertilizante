
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('lista_tipo_cultivo/', views.ListaTipoCultivo.as_view(), name='lista_tipo_cultivo'),
    path('nuevo_tipo_cultivo/', views.NuevoTipoCultivo.as_view(), name='nuevo_tipo_cultivo'),
    path('editar_tipo_cultivo/<int:pk>', views.EditarTipoCultivo.as_view(), name='editar_tipo_cultivo'),
    path('eliminar_tipo_cultivo/<int:pk>', views.EliminarTipoCultivo.as_view(), name='eliminar_tipo_cultivo'),
    path('lista_cultivo/', views.ListaCultivo.as_view(), name='lista_cultivo'),
    path('nuevo_cultivo/', views.NuevoCultivo.as_view(), name='nuevo_cultivo'),
    path('editar_cultivo/<int:pk>', views.EditarCultivo.as_view(), name='editar_cultivo'),
    path('eliminar_cultivo/<int:pk>', views.EliminarCultivo.as_view(), name='eliminar_cultivo'),
]
