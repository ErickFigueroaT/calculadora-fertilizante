from django.db import models

# Create your models here.

class TipoCultivo(models.Model):
    nombre = models.CharField( max_length = 50)

    def str(self) :
        return self.nombre

class Cultivo(models.Model):
    nombre = models.CharField( max_length = 50)
    tipo_cultivo = models.ForeignKey("calculadora.TipoCultivo", verbose_name="Tipo Cultivo", on_delete=models.CASCADE)

    def str(self) :
        return self.nombre

class PropiedadesSuelo(models.Model):
    # TODO falta agregar las propiedades del suelo
    pass

class GenerarCalculo(models.Model):
    cultivo = models.ForeignKey('calculadora.Cultivo', verbose_name='Cultivo', on_delete=models.DO_NOTHING)
    propiedades_suelo = models.ForeignKey('calculadora.PorpiedadesSuelo', verbose_name='Propiedades Suelo', on_delete=models.DO_NOTHING)
    usuario = models.ForeignKey('usuarios.Usuario', verbose_name='Usuario', on_delete=models.DO_NOTHING)
    # TODO falta agregar toda la inforamcion del calculo