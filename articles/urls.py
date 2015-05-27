from django.conf.urls import url
from .views import ListaArticulos, ArticuloDetallado

urlpatterns = [
    url(r'^$', ListaArticulos.as_view(), name="lista_entradas"),
    url(r'^(?P<slug>[-\w]+)/$', ArticuloDetallado.as_view(), name="detalle"),
]
