from django.db import models

# Create your models here.

class Perro(models.Model):
    raza = models.CharField(max_length=100)
    edad = models.IntegerField()
    peso = models.DecimalField(max_digits=5, decimal_places=2)

class Gato(models.Model):
    raza = models.CharField(max_length=100)
    edad = models.IntegerField()
    peso = models.DecimalField(max_digits=5, decimal_places=2)

class Exotico(models.Model):
    raza = models.CharField(max_length=100)
    edad = models.IntegerField()
    peso = models.DecimalField(max_digits=5, decimal_places=2)