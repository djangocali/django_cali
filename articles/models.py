from django.db import models
from taggit.managers import TaggableManager
from django.template.defaultfilters import slugify
from django.conf import settings


class Categoria(models.Model):
    creado_en = models.DateTimeField(auto_now_add=True)
    modificado_en = models.DateTimeField(auto_now=True)
    nombre = models.CharField(max_length=20, unique=True, null=False)
    slug = models.SlugField(max_length=50, null=True, blank=True,
                            editable=False)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.nombre)

        super(Categoria, self).save(*args, **kwargs)


class Articulo(models.Model):
    ESTADO = (
        ('b', 'borrador'),
        ('p', 'publicado'),
    )
    creado_en = models.DateTimeField(auto_now_add=True, editable=False)
    modificado_en = models.DateTimeField(auto_now=True)
    titulo = models.CharField(max_length=50, null=False, unique=True)
    imagen_destacada = models.ImageField(upload_to='main_pics/')
    contenido = models.TextField(null=False)
    autor = models.ForeignKey(settings.AUTH_USER_MODEL)
    categoria = models.ForeignKey(Categoria)
    tags = TaggableManager()
    slug = models.SlugField(max_length=50, null=True, blank=True,
                            editable=False)
    estado = models.CharField(max_length=1, choices=ESTADO, default='p')

    class Meta:
        verbose_name = "Articulo"
        verbose_name_plural = "Articulos"
        ordering = ('-creado_en',)

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.titulo)

        super(Articulo, self).save(*args, **kwargs)
