from rest_framework import generics
from core.models import Livro, Categoria, Autor
from core.serializers import LivroSerializer, CategoriaSerializer, AutorSerializer
from core.filters import LivroFilter

class LivroList(generics.ListCreateAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    name='livros-list'
    filterset_class = LivroFilter
    search_fields = ("^name")
    ordering_fields = ['titulo', 'autor', 'categoria', 'publicado_em']

class LivroDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    name = "livro-detail"

class CategoriaList(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    name = "categoria-list"
    search_fields = ("^name",)
    ordering_fields = ("name",)

class CategoriaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    name = "categoria-detail"

class AutorList(generics.ListCreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    name = "autor-list"
    search_fields = ("^name",)
    ordering_fields = ("name",)

class AutorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    name = "autor-detail"
