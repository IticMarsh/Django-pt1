from django.db import models

# Create your models here.
# models.py

class Rol(models.Model):
    nom = models.CharField(max_length=100)

class Usuari(models.Model):
    nom = models.CharField(max_length=100)
    cognom = models.CharField(max_length=100)
    assignatures = models.CharField(max_length=255)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)

class AssignaturesImpartides(models.Model):
    usuari = models.ForeignKey(Usuari, on_delete=models.CASCADE)
    assignatura = models.CharField(max_length=100)

