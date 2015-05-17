from django.shortcuts import render
from django.views.generic import ListView  # , DetailView
from .models import Entrada
# Create your views here.


class Mis_entradas(ListView):
    model = Entrada
    template_name = 'entradas.html'
    context_object_name = 'entrada'

"""class Detalle(DetailView):
    model = Entrada
    template = 'detalle.html'
    context_object_name = 'detalle'
"""


def detalle(request, pk):
    cont = Entrada.objects.get(pk=pk)
    return render(request, 'detalle.html', locals())

# Crear todas las vistas usando ClassBased Views

# Crear vista que lista las ultimas cinco entradas

# Crear vista que muestre las entradas mas populares

# Crear vista que invoca todas las entradas

# Crear vista que lista todas las entradas de una categoria dada

# Crear vista que muestre las entradas de una etiqueta dada
