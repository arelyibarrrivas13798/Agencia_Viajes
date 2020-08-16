from django.db import models

# Create your models here.

class Destinos(models.Model):
    title = models.CharField('titulo', max_length=50)
    description = models.CharField('descripcion', max_length=100)
    images = models.ImageField(upload_to='viajes/images')
    puntuation = models.CharField('puntaje', max_length=2)
    coments = models.TextField('comentarios',  max_length=200)
    restaurant = models.TextField('restaurantes', max_length=200)
