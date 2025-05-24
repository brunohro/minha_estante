from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=200)
    def __str__(self):
        return self.nome

class Autor(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome
class Livro(models.Model):
    STATUS_CHOICES = [
        ('lido', 'Lido'),
        ('lendo', 'Lendo'),
        ('quero_ler', 'Quero Ler'),
    ]
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='quero_ler'
    )
    imagem = models.ImageField(upload_to='livros/', blank=True, null=True)
    data_inicio = models.DateField()
    data_fim = models.DateField()


