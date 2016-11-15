from __future__ import unicode_literals

from django.db import models
from django.conf import settings
# Create your models here.

class Curso(models.Model):
    """ Modelo curso define los tipos de campos que necesita en la BD """
    autor = models.ForeignKey(settings.AUTH_USER_MODEL)
    creado_el = models.DateTimeField(auto_now_add=True)
    titulo = models.CharField(max_length=160)
    descripcion = models.TextField()

    def __unicode__(self):
        return self.titulo

class Paso(models.Model):
    """ Modelo para los pasos que tiene cada curso """
    titulo = models.CharField(max_length=160)
    descripcion = models.TextField()
    orden = models.IntegerField(default=0)
    curso = models.ForeignKey(Curso, related_name='pasos')

    def __unicode__(self):
        return self.titulo
