from django.urls import path
from coglivros.views import home, livros

urlpatterns = [
    path('home/', home, name='home'),
    path('livros/<int:livro_id>', livros, name='livros')
]