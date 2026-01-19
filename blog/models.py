from django.db import models


class Autor(models.Model):
    nome = models.CharField(max_length=80)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome


class Categoria(models.Model):
    titulo = models.CharField(max_length=60, unique=True)

    def __str__(self):
        return self.titulo


class Post(models.Model):
    titulo = models.CharField(max_length=120)
    conteudo = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)

    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.titulo
