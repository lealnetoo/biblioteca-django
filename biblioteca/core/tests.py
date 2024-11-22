from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Autor, Livro, Colecao

class ColecaoTests(APITestCase):
    def setUp(self):
        # Cria um usuário
        self.user = User.objects.create_user(username='testuser', password='12345')
        # Cria um autor
        self.autor = Autor.objects.create(nome="Autor Teste")
        # Cria um livro associando ao autor
        self.livro = Livro.objects.create(titulo="Livro Teste", autor=self.autor, publicado_em="2024-01-01")

    def test_criar_colecao_autenticado(self):
        self.client.login(username='testuser', password='12345')
        data = {
            'nome': 'Minha Coleção',
            'descricao': 'Teste de criação',
            'livros': [self.livro.id],
        }
        response = self.client.post('/colecoes/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_criar_colecao_nao_autenticado(self):
        data = {
            'nome': 'Minha Coleção',
            'descricao': 'Teste de criação',
            'livros': [self.livro.id],
        }
        response = self.client.post('/colecoes/', data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_editar_colecao_de_outro_usuario(self):
        user2 = User.objects.create_user(username='user2', password='12345')
        colecao = Colecao.objects.create(
            nome="Coleção de Outro",
            colecionador=user2,
            descricao="Teste de edição",
        )
        self.client.login(username='testuser', password='12345')
        data = {'nome': 'Nova Coleção'}
        response = self.client.put(f'/colecoes/{colecao.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
