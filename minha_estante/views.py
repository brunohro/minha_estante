from django.shortcuts import render, redirect
from .models import Livro
from .forms import LivroForm
def index(request):
    livros = Livro.objects.all()
    return render(request, "minha_estante/index.html", {'livros': livros})


def cadastrar_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = LivroForm()
    return render(request, "minha_estante/livros/cadastrar_livro.html", {'form': form})
