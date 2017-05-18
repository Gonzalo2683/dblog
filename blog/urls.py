from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='detalle_post'),
    url(r'^posts/$', views.PostListApi.as_view(), name='post_list_api')
]