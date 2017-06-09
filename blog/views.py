from django.shortcuts import render, get_object_or_404
from blog import models
from .forms import ComentarioForm
from django import http

from rest_framework import generics
from rest_framework import viewsets

from blog import serializers

# Create your views here.
def post_list(request):
    entradas = models.Post.objects.all()
    return render(request, 'blog/post_list.html', {'entradas': entradas})


def post_detail(request, pk):
    post = get_object_or_404(models.Post, pk=pk)

    #cometarios
    comentarios = post.comentarios.filter(activo=True)
    if request.method == 'POST':
        cometario_form = ComentarioForm(data=request.POST)
        if cometario_form.is_valid():
            nuevo_comentario = cometario_form.save(commit=False)
            nuevo_comentario.post = post
            nuevo_comentario.save()
    else:
        cometario_form = ComentarioForm()

    return render(request, 'blog/post_detail.html', {'post': post, 'comentarios': comentarios, 'cometario_form': cometario_form})

# API VIEWS
class ListCreatePost(generics.ListCreateAPIView):
    queryset = models.Post.published.all()
    serializer_class = serializers.PostSerializer
    
    
class RetriveUpdateDestroyPost(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Post.published.all()
    serializer_class = serializers.PostSerializer
    
    
class ListCreateComentario(generics.ListCreateAPIView):
    queryset = models.Comentario.objects.all()
    serializer_class = serializers.ComentSerializer
    
    def get_queryset(self):
        return self.queryset.filter(post_id=self.kwargs.get('post_pk'))


class RetriveUpdateDestroyComentario(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Comentario.objects.all()
    serializer_class = serializers.ComentSerializer
    
    def get_object(self):
        return get_object_or_404(
            self.get_queryset(),
            post_id=self.kwargs.get('post_pk'),
            pk=self.kwargs.get('pk')
            )