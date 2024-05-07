
from django.contrib import admin
from django.urls import path, include
from calculadora.views import BienvenidaView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('calculadora/', include ('calculadora.urls')),
    path('usuario/', include ('usuario.urls')),
    path('cultivos/', include('cultivos.urls')),
    path('', BienvenidaView.as_view(), name='bienvenida'),
]
