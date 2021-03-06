from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='publicado')

class Post(models.Model):
    """ Modelo post """
    STATUS_ENTRADA = (
        ('borrador', 'Borrador'),
        ('publicado', 'Publicado'),
    )
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='usuario')
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    creado_el = models.DateTimeField(default=timezone.now)
    publicado_el = models.DateTimeField(blank=True, null=True)

    status = models.CharField(max_length=10, choices=STATUS_ENTRADA, default='borrador')

    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager.

    class Meta:
        ordering = ('publicado_el',)

    def publicar(self):
        """ Gaurda y actualiza fecha de publicacion """
        self.publicado_el = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    """ Modelo para comments """
    post = models.ForeignKey(Post, related_name='comentarios')
    nombre = models.CharField(max_length=80)
    email = models.EmailField()
    mensaje = models.TextField()
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=True)

    class Meta:
        ordering = ['creado',]

    def __str__(self):
        return 'Comentario por {} en {}'.format(self.nombre, self.post)

