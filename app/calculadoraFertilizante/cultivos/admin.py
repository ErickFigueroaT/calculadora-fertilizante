from django.contrib import admin

from .models import TipoCultivo
from .models import Cultivo

admin.site.register(TipoCultivo)
admin.site.register(Cultivo)