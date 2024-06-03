from django.contrib import admin
from coglivros.models import Livro

class ListandoLivros(admin.ModelAdmin):
    list_display = ("id", "nome", "autor", "genero","publicada")
    list_display_links = ("id", "nome")
    search_fields = ("nome",)
    list_filter = ("genero",)
    list_editable = ("publicada",)
    list_per_page = 10

admin.site.register(Livro, ListandoLivros)
