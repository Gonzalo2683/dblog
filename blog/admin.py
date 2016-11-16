from django.contrib import admin
from .models import Post, Comentario
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'creado_el', 'publicado_el', 'status']

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'email', 'post', 'creado', 'activo']
