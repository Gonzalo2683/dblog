from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.ListCreatePost.as_view(), name='post_list'),
    url(r'(?P<pk>\d+)/$', views.RetriveUpdateDestroyPost.as_view(), name='post_detalle'),
    url(r'^(?P<post_pk>\d+)/comentarios/$', views.ListCreateComentario.as_view(), name='comentario_list'),
    url(r'^(?P<post_pk>\d+)/comentarios/(?P<pk>\d+)/$', views.RetriveUpdateDestroyComentario.as_view(), name='comentario_detalle'),
]