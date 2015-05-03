from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


class Entrada(models.Model):
    creado_en = models.DateTimeField(auto_now_add=True)
    modificado_en = models.DateTimeField(auto_now=True)
    titulo = models.CharField(max_lenght=50, null=False, unique=True)
    contenido = models.TextField(null=False)
    slug = models.SlugField(max_length=50)
    autor = models.ForeignKey(User)

    class Meta:
        verbose_name = "Entrada"
        verbose_name_plural = "Entradas"

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.titulo)

        super(Entrada, self).save(*args, **kwargs)
