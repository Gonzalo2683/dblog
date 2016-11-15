from django.shortcuts import render
from django.views.generic import ListView
from .models import Curso


# Create your views here.
class ListadoCursos(ListView):
    model = Curso
    template_name = 'cursos/listado_cursos.html'

