from rest_framework import serializers
from .models import Categoria, Autor, Livro, Colecao

class CategoriaSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nome = serializers.CharField(max_length=100)
    
    def create(self, validated_data):
        return Categoria.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.nome = validated_data.get('nome', instance.nome)
        instance.save()
        return instance
    
class AutorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nome = serializers.CharField(max_length=100)
    
    def create(self, validated_data):
        return Autor.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.nome = validated_data.get('nome', instance.nome)
        instance.save()
        return instance
    
class LivroSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    titulo = serializers.CharField(max_length=200)
    autor = serializers.PrimaryKeyRelatedField(queryset=Autor.objects.all())
    categoria = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all())
    publicado_em = serializers.DateField()
 
    def create(self, validated_data):
        return Livro.objects.create(**validated_data)
 
    def update(self, instance, validated_data):
        instance.titulo = validated_data.get('titulo', instance.titulo)
        instance.autor = validated_data.get('autor', instance.autor)
        instance.categoria = validated_data.get('categoria', instance.categoria)
        instance.publicado_em = validated_data.get('publicado_em', instance.publicado_em)
        instance.save()
        return instance
    
class ColecaoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nome = serializers.CharField(max_length=100)
    descricao = serializers.CharField(required=False, allow_blank=True)
    livros = serializers.PrimaryKeyRelatedField(
        queryset=Livro.objects.all(),
        many=True  # Permite associar múltiplos livros à coleção
    )
    colecionador = serializers.PrimaryKeyRelatedField(read_only=True)

    def create(self, validated_data):
        livros = validated_data.pop('livros')  # Retira livros dos dados validados
        colecao = Colecao.objects.create(**validated_data)  # Cria a coleção
        colecao.livros.set(livros)  # Associa os livros
        return colecao

    def update(self, instance, validated_data):
        instance.nome = validated_data.get('nome', instance.nome)
        instance.descricao = validated_data.get('descricao', instance.descricao)
        
        if 'livros' in validated_data:
            livros = validated_data.pop('livros')
            instance.livros.set(livros)  # Atualiza os livros associados
        
        instance.save()  # Salva as alterações
        return instance