from django.contrib import admin
from django.urls import path, include
from . import views  # Importa las vistas desde el directorio actual

urlpatterns = [
    # Rutas para gestionar los tipos de cultivo
    path('lista_tipo_cultivo/', views.ListaTipoCultivo.as_view(), name='lista_tipo_cultivo'),
    # Ruta para mostrar una lista de tipos de cultivo
    path('nuevo_tipo_cultivo/', views.NuevoTipoCultivo.as_view(), name='nuevo_tipo_cultivo'),
    # Ruta para crear un nuevo tipo de cultivo
    path('editar_tipo_cultivo/<int:pk>', views.EditarTipoCultivo.as_view(), name='editar_tipo_cultivo'),
    # Ruta para editar un tipo de cultivo existente
    path('eliminar_tipo_cultivo/<int:pk>', views.EliminarTipoCultivo.as_view(), name='eliminar_tipo_cultivo'),
    # Ruta para eliminar un tipo de cultivo existente

    # Rutas para gestionar los cultivos
    path('lista_cultivo/', views.ListaCultivo.as_view(), name='lista_cultivo'),
    # Ruta para mostrar una lista de cultivos
    path('nuevo_cultivo/', views.NuevoCultivo.as_view(), name='nuevo_cultivo'),
    # Ruta para crear un nuevo cultivo
    path('editar_cultivo/<int:pk>', views.EditarCultivo.as_view(), name='editar_cultivo'),
    # Ruta para editar un cultivo existente
    path('eliminar_cultivo/<int:pk>', views.EliminarCultivo.as_view(), name='eliminar_cultivo'),
    # Ruta para eliminar un cultivo existente
]

