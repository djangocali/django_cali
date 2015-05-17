from django.shortcuts import render


def inicio(request):
    # mensaje = "Bienvenidos a mi pagina"
    # template = "index.html"

    # return render(request, template, {'mensaje': mensaje, })
    return render(request, "index.html", {})
