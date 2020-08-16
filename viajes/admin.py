from django.contrib import admin
from viajes.models import Destinos
# Register your models here.
# admin.site.register(Recipes)

"""Añade vista al admin"""


@admin.register(Destinos)
class viajeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'images', 'puntuation')
    list_display_links = ('pk', 'images')
    list_editable = ('title', 'puntuation')