from django.views.generic import ListView, DetailView
from .models import Articulo
# Create your views here.


class ListaArticulos(ListView):
    model = Articulo
    template_name = 'articulos.html'
    context_object_name = 'articulos'


class ArticuloDetallado(DetailView):
    model = Articulo
    template_name = 'articulo-detallado.html'

    def get_context_data(self, **kwargs):
        context = super(ArticuloDetallado, self).get_context_data(**kwargs)
        return context
