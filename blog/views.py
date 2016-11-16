from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import ComentarioForm
from django import http

# Create your views here.
def post_list(request):
    entradas = Post.objects.all()
    return render(request, 'blog/post_list.html', {'entradas': entradas})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

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
