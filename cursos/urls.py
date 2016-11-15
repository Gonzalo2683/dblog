from django.conf.urls import url
from .views import ListadoCursos


urlpatterns = [
    url(r'^$', ListadoCursos.as_view())
]