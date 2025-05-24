from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=200)
    def __str__(self):
        return self.nome

class Autores(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome
class Livro(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField(max_length=200)
    autor = models.ForeignKey(Autores, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    is_completed = models.BooleanField()
    imagem = models.ImageField(upload_to='livros/', blank=True, null=True)
    data_inicio = models.DateField()
    data_fim = models.DateField()


