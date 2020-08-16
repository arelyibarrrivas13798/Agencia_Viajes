from django.contrib import admin

# Register your models here.

class Places(models.Model):
    place = models.CharField('lugar', max_length=50)
    description = models.CharField('descripcion', max_length=100)
    images = models.ImageField(upload_to='viajes/images')
    recommended = models.CharField('recomendado', max_length=2)
    comments = models.TextField('comentarios',  max_length=200)
    weather = models.TextField('clima', max_length=100)