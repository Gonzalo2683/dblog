from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def post_list(request):
    entradas = Post.objects.all()
    return render(request, 'blog/post_list.html', {'entradas': entradas})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
