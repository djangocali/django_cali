from django.conf.urls import url
from .views import PerfilDetallado, ListaPerfiles

urlpatterns = [
    url(r'^$', ListaPerfiles.as_view(), name="lista-perfiles"),
    url(r'^perfil/(?P<pk>[\d]+)/$', PerfilDetallado.as_view(), name='perfil-detallado'),
]
