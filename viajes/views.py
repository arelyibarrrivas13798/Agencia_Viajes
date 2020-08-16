from django.shortcuts import render
from viajes.models import Destinos

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.generic import View
from django.conf.urls.static import static
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
# Create your views here.

def index(request):
    return render(request, 'viajes/Destinos.html')

def agregar(request):
    """Verica si es post"""
    if request.method == 'POST':
        title = request.POST['input_title']
        description = request.POST['input_description']
        images = request.FILES['file_images']
        puntuation = request.POST['input_puntuation']
        coments = request.POST['input_coments']
        restaurant = request.POST['input_restaurant']

        viaje = Destinos.objects.create(
            title=title, description=description)
        viaje.coments = coments
        viaje.restaurant = restaurant
        viaje.images = images
        viaje.puntuation = puntuation
        viaje.save()
        return redirect('viajes:index')

    """renderiza la vista aunque no sea post"""
    return render(request, 'viajes/agregar.html')


def recetario(request):
    recipes = Recipes.objects.all()
    return render(request, 'recipes/recetario.html', {'recipes': recipes})

def hotel(request):
    return render(request, 'viajes/hotel.html')

def lugares(request):
    viajes = Destinos.objects.all()
    return render(request, 'viajes/lugares.html', {'viajes': viajes})

def recomendados(request):
    return render(request, 'viajes/recomendados.html')