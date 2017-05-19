from rest_framework import serializers
from blog import models

class ComentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comentario
        fields = ('nombre', 'email', 'mensaje')

class PostSerializer(serializers.ModelSerializer):
    comentarios = ComentSerializer(many=True, read_only=True)
    full_autor = serializers.SerializerMethodField()                                                              

    def get_full_autor(self, obj):                                                                                                  
        return {
            'nombre': obj.autor.first_name,
            'apellido': obj.autor.last_name
        }
    class Meta:
        model = models.Post
        fields = (
            'full_autor','titulo', 'contenido', 'creado_el', 'publicado_el', 'status', 'comentarios'
        )
