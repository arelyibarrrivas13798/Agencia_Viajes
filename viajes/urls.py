from django.urls import path
from viajes import views
from django.conf.urls.static import static
from django.conf import settings

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from viajes.models import Destinos
from django.views.generic import View
from django.conf.urls.static import static
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders

# from .views import generatePdf

"""Urls de recetas"""
urlpatterns = [
    path(route='', view=views.index, name='index'),
    path(route='agregar/', view=views.agregar, name='agregar'),
    path(route='hoteles/', view=views.hotel, name='hotel'),
    path(route='recomendados/', view=views.recomendados, name='recomendados'),
    path(route='lugares/', view=views.lugares, name='lugares'),
]