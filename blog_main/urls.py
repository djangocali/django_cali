from django.conf.urls import url
from .views import ListaEntradas, EntradaDetallada

urlpatterns = [
    url(r'^$', ListaEntradas.as_view(), name="lista_entradas"),
    url(r'^(?P<slug>[-\w]+)/$', EntradaDetallada.as_view(), name="detalle"),
]
