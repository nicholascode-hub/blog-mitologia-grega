from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome

class Deus(models.Model):
    nome = models.CharField(max_length=200)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='deuses/', blank=True, null=True)
    familia = models.TextField(blank=True)
    atributos = models.TextField(blank=True)
    mitos = models.TextField(blank=True)

    def __str__(self):
        return self.nome
