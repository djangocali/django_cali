from django.views.generic import ListView, DetailView
from .models import Entrada
# Create your views here.


class ListaEntradas(ListView):
    model = Entrada
    template_name = 'entradas.html'
    context_object_name = 'entrada'


class EntradaDetallada(DetailView):
    model = Entrada
    template_name = 'entrada-detallada.html'

    def get_context_data(self, **kwargs):
        context = super(EntradaDetallada, self).get_context_data(**kwargs)
        return context

# Crear todas las vistas usando ClassBased Views

# Crear vista que lista las ultimas cinco entradas

# Crear vista que muestre las entradas mas populares

# Crear vista que invoca todas las entradas

# Crear vista que lista todas las entradas de una categoria dada

# Crear vista que muestre las entradas de una etiqueta dada
