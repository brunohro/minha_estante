from django.shortcuts import render
from .models import Livro
def index(request):
    livros = Livro.objects.all()
    return render(request, "minha_estante/index.html", {'livros': livros})
