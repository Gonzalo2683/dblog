""" Se gestionan los modelos y su interaccion con el admin """
from django.contrib import admin
from .models import Curso, Paso

# Register your models here.
class PasoInline(admin.StackedInline):
    """ Define al modelo paso como inline """
    model = Paso

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    """ Registra en el admin el modelo cursos, inline paso """
    inlines = [PasoInline,]
    list_display = ['titulo', 'autor']

@admin.register(Paso)
class PasoAdmin(admin.ModelAdmin):
    """ Registra en el admin el modelo Paso """
    list_display = ['titulo', 'curso', 'orden']
