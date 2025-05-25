from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Livro
from .forms import LivroForm

def cadastrar_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = UserCreationForm()
    return render(request, "minha_estante/user/cadastrar_usuario.html", {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'minha_estante/user/login.html', {'error': 'Usuário ou senha inválidos'})
    return render(request, 'minha_estante/user/login.html')

def logout_view(request):
    logout(request)
    return render(request, "minha_estante/index.html")

@login_required
def index(request):
    livros = Livro.objects.all()
    return render(request, "minha_estante/index.html", {'livros': livros})

@login_required
def cadastrar_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = LivroForm()
    return render(request, "minha_estante/livros/cadastrar_livro.html", {'form': form, 'editar': False})

@login_required
def editar_livro(request, id):
    livro = Livro.objects.get(id=id)
    if request.method == 'POST':
        form = LivroForm(request.POST, request.FILES, instance=livro)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = LivroForm(instance=livro)
    return render(request, "minha_estante/livros/cadastrar_livro.html", {'form': form, 'editar': True})

@login_required
def deletar_livro(request, id):
    livro = Livro.objects.get(id=id)
    livro.delete()
    return redirect('index')