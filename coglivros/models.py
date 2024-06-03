from django.db import models

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
    foto =  models.CharField(max_length=100, null=False, blank=False)
    publicada = models.BooleanField(default=False)

    def __str__(self):
        return self.nome
