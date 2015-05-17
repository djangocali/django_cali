from django.views.generic import DetailView, ListView
from .models import UserProfile


class ListaPerfiles(ListView):
    model = UserProfile
    template_name = 'perfiles.html'

    def get_context_data(self, **kwargs):
        context = super(ListaPerfiles, self).get_context_data(**kwargs)
        return context


class PerfilDetallado(DetailView):
    model = UserProfile
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super(PerfilDetallado, self).get_context_data(**kwargs)
        return context
