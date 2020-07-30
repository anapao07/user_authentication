from django.db import models

# Create your models here.
class Cultivo(models.Model):
    nombre = models.CharField(max_length=256)
    agua = models.CharField(max_length=256)
    energia = models.CharField(max_length=256)
    quimico = models.CharField(max_length=256)

    def __str__(self):
        return self.nombre