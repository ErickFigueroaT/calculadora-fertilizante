from django.db import models

# Create your models here.

class TipoCultivo(models.Model):
    nombre = models.CharField( max_length = 50)

    def __str__(self) :
        return self.nombre

class Cultivo(models.Model):
    nombre = models.CharField( max_length = 50)
    tipo_cultivo = models.ForeignKey("cultivos.TipoCultivo", verbose_name="Tipo Cultivo", on_delete=models.CASCADE)

    def __str__(self) :
        return self.nombre