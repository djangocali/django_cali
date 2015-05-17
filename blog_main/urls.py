from django.conf.urls import url
from .views import Mis_entradas, detalle

urlpatterns = [
    url(r'^resultados/$', Mis_entradas.as_view(), name="resultados"),
    url(r'^resultados/((?P<pk>[\d]+))/$', detalle, name="detalle"),
]
