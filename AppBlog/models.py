from django.db import models

# Create your models here.
class Platos(models.Model):
    nombre = models.CharField(max_length=40)
    pais = models.CharField(max_length=30)
    fecha = models.DateField()
    cocinero = models.CharField(max_length=40)
    receta = models.TextField()

class Postres(models.Model):
    nombre = models.CharField(max_length=40)
    pais = models.CharField(max_length=40)
    fecha = models.DateField()
    pastelero = models.CharField(max_length=40)

class Cafe(models.Model):
    variedad = models.CharField(max_length=40)
    filtrado = models.CharField(max_length=40)
    barista = models.CharField(max_length=40)
    origen = models.CharField(max_length=40)

class Vino(models.Model):
    varietal = models.CharField(max_length=40)
    origen = models.CharField(max_length=40)
    fecha = models.DateField()
    temperatura = models.IntegerField()

class Quesos(models.Model):
    nombre = models.CharField(max_length=40)
    tipo = models.CharField(max_length=40)
    origen = models.CharField(max_length=40)
    pasteurizado = models.BooleanField()
