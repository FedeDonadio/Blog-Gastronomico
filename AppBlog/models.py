#from dataclasses import fields
#from msilib.schema import ListView
from django.db import models
from django.urls import reverse

# Create your models here.
class Platos(models.Model):
    nombre = models.CharField(max_length=40)
    fecha = models.DateField()
    cocinero = models.CharField(max_length=40)
    receta = models.TextField() 

    def get_absolute_url(self):
        return reverse("platos", kwargs={"pk": self.pk})

    def __str__(self):
        return f"nombre: {self.nombre} - fecha: {self.fecha} - cocinero: {self.cocinero} - receta: {self.receta}"



class Postres(models.Model):
    nombre = models.CharField(max_length=40)
    pais = models.CharField(max_length=40)
    fecha = models.DateField()
    pastelero = models.CharField(max_length=40)

<<<<<<< HEAD
    def get_absolute_url(self):
        return reverse("postres", kwargs={"pk": self.pk}) 

    def __str__(self):
        return f"nombre: {self.nombre} - pais: {self.pais} - fecha: {self.fecha} - pastelero: {self.pastelero}"    
    


=======
    def __str__(self):
        return f"nombre: {self.nombre} - pais: {self.pais} - fecha: {self.fecha} - pastelero: {self.pastelero}"
>>>>>>> 3ba5825c822415047ffaf83b6d2b423489240317

class Cafe(models.Model):
    variedad = models.CharField(max_length=40)
    filtrado = models.CharField(max_length=40)
    barista = models.CharField(max_length=40)
    origen = models.CharField(max_length=40)

<<<<<<< HEAD
    def get_absolute_url(self):
        return reverse("cafe", kwargs={"pk": self.pk}) 

    def __str__(self):
        return f"variedad: {self.variedad} - filtrado: {self.filtrado} - barista: {self.barista} - origen: {self.origen}"    


=======
    def __str__(self):
        return f"variedad:{self.variedad} - filtrado:{self.filtrado} - barista: {self.barista} - origen:{self.origen}"
    
>>>>>>> 3ba5825c822415047ffaf83b6d2b423489240317

class Vino(models.Model):
    varietal = models.CharField(max_length=40)
    origen = models.CharField(max_length=40)
    fecha = models.DateField()
    temperatura = models.IntegerField() 

    def get_absolute_url(self):
        return reverse("vinos", kwargs={"pk": self.pk}) 

    def __str__(self):
        return f"varietal: {self.varietal} - origen: {self.origen} - fecha: {self.fecha} - temperatura: {self.temperatura}"    




    def __str__(self):
        return f"variedad:{self.varietal} - origen:{self.origen} - fecha:{self.fecha} - temperatura:{self.temperatura}"
    

class Quesos(models.Model):
    nombre = models.CharField(max_length=40)
    tipo = models.CharField(max_length=40)
    origen = models.CharField(max_length=40)
<<<<<<< HEAD
    pasteurizado = models.BooleanField() 

    def get_absolute_url(self):
        return reverse("postres", kwargs={"pk": self.pk}) 

    def __str__(self):
        return f"nombre: {self.nombre} - tipo: {self.tipo} - origen: {self.origen} - pasteurizado: {self.pasteurizado}"    
=======
    pasteurizado = models.BooleanField()

    def __str__(self):
        return f"nombre:{self.nombre} - tipo:{self.tipo} - origen:{self.origen} - pasteurizado:{self.pasteurizado} "
    
>>>>>>> 3ba5825c822415047ffaf83b6d2b423489240317
