from django import forms
from .models import Livro, Categoria, Autor

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['nome', 'descricao', 'autor', 'categoria', 'status', 'imagem', 'data_inicio', 'data_fim']
