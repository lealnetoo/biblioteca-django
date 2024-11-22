from django.urls import path
from . import views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


urlpatterns = [
    # URLs para Livro
    path('livros/', views.LivroList.as_view(), name='livros-list'),
    path('livros/<int:pk>/', views.LivroDetail.as_view(), name='livro-detail'),
    
    # URLs para Categoria
    path('categorias/', views.CategoriaList.as_view(), name='categorias-list-create'),
    path('categorias/<int:pk>/', views.CategoriaDetail.as_view(), name='categoria-detail'),
    
    # URLs para Autor
    path('autores/', views.AutorList.as_view(), name='autores-list-create'),
    path('autores/<int:pk>/', views.AutorDetail.as_view(), name='autor-detail'),

    path("colecoes/", views.ColecaoListCreate.as_view(), name="colecao-list"),
    path("colecoes/<int:pk>/", views.ColecaoDetail.as_view(), name="colecao-detail"),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='api-docs'),
]
