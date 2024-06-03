from django.shortcuts import render,get_object_or_404
from coglivros.models import Livro

def home(request):
    livros = Livro.objects.order_by("data_publicacao").filter(publicada=True)

    return render(request, 'coglivros/home.html', {"livros": livros})

def livros(request, livro_id):
    livro = get_object_or_404(Livro, pk=livro_id)
    return render(request, 'coglivros/livros.html', {"livro": livro})


def buscar(request):
    livros = Livro.objects.order_by("data_publicacao").filter(publicada=True)

    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            livros = livros.filter(genero__icontains=nome_a_buscar)

    return render(request, "coglivros/buscar.html", {"livros": livros})