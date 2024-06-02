from django.shortcuts import render
from coglivros.models import Livro

def home(request):
    livros = Livro.objects.all()
    return render(request, 'coglivros/home.html', {"livros": livros})
