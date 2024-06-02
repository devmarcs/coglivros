from django.db import models

class Livro(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    genero = models.CharField(max_length=50, null=False, blank=False)
    autor = models.CharField(max_length=100, null=False, blank=False)
    sinopse = models.TextField(null=False, blank=False)
    foto =  models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.nome
