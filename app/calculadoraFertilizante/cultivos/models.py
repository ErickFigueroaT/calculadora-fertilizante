from django.db import models

# Create your models here.

class TipoCultivo(models.Model):
    nombre = models.CharField( max_length = 50)

    def __str__(self) :
        return self.nombre

class Cultivo(models.Model):
    nombre = models.CharField( max_length = 50)
    tipo_cultivo = models.ForeignKey("cultivos.TipoCultivo", verbose_name="Tipo Cultivo", on_delete=models.CASCADE)
    N = models.FloatField(default=0.0)
    P = models.FloatField(default=0.0)
    K = models.FloatField(default=0.0)
    Ca = models.FloatField(default=0.0)
    Mg = models.FloatField(default=0.0)
    S = models.FloatField(default=0.0)
    B = models.FloatField(default=0.0)
    Cl = models.FloatField(default=0.0)
    Cu = models.FloatField(default=0.0)
    Fe = models.FloatField(default=0.0)
    Mn = models.FloatField(default=0.0)
    Mo = models.FloatField(default=0.0)
    Zn = models.FloatField(default=0.0)
    Ni = models.FloatField(default=0.0)
    #para el IC de cada elemento
    icN = models.FloatField(default=0.0)
    icP = models.FloatField(default=0.0)
    icK = models.FloatField(default=0.0)
    icCa = models.FloatField(default=0.0)
    icMg = models.FloatField(default=0.0)
    icS = models.FloatField(default=0.0)
    icB = models.FloatField(default=0.0)
    icCl = models.FloatField(default=0.0)
    icCu = models.FloatField(default=0.0)
    icFe = models.FloatField(default=0.0)
    icMn = models.FloatField(default=0.0)
    icMo = models.FloatField(default=0.0)
    icZn = models.FloatField(default=0.0)
    icNi = models.FloatField(default=0.0)
    def __str__(self) :
        return self.nombre