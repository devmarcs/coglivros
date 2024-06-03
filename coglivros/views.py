from django.shortcuts import render,get_object_or_404
from coglivros.models import Livro

def home(request):
    livros = Livro.objects.filter(publicada=True)

    return render(request, 'coglivros/home.html', {"livros": livros})

def livros(request, livro_id):
    livro = get_object_or_404(Livro, pk=livro_id)
    return render(request, 'coglivros/livros.html', {"livro": livro})