from django.db import models
from datetime import datetime   

class Livro(models.Model):

    OPCOES_GENERO = [
        ("ROMANCE", "romance"),
        ("AVENTURA", "aventura"),
        ("SUSPENSE", "suspense"),
        ("FICÇÃO", "ficção"),
    ]

    nome = models.CharField(max_length=100, null=False, blank=False)
    genero = models.CharField(max_length=50, choices=OPCOES_GENERO, default="")
    autor = models.CharField(max_length=100, null=False, blank=False)
    sinopse = models.TextField(null=False, blank=False)
    foto =  models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
    publicada = models.BooleanField(default=False)
    data_publicacao = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        return self.nome
