from rest_framework import serializers

from blog import models

class ComentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comentario
        fields = ('nombre', 'email', 'mensaje')

class PostSerializer(serializers.ModelSerializer):
    comentarios = ComentSerializer(many=True, read_only=True)

    class Meta:
        fields = (
            'autor', 'titulo', 'contenido', 'creado_el', 'publicado_el', 'status', 'comentarios'
        )
        model = models.Post
