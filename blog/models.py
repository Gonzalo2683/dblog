from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.

class Post(models.Model):
    """ Modelo post """
    STATUS_ENTRADA = (
        ('borrador', 'Borrador'),
        ('publicado', 'Publicado'),
    )
    autor = models.ForeignKey(settings.AUTH_USER_MODEL)
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    creado_el = models.DateTimeField(default=timezone.now)
    publicado_el = models.DateTimeField(blank=True, null=True)

    status = models.CharField(max_length=10, choices=STATUS_ENTRADA, default='borrador')

    def publicar(self):
        """ Gaurda y actualiza fecha de publicacion """
        self.publicado_el = timezone.now()
        self.save()

    def __unicode__(self):
        return self.titulo
