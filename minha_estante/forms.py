from django import forms
from .models import Livro, Categoria, Autor

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['nome', 'descricao', 'autor', 'categoria', 'status', 'imagem', 'data_inicio', 'data_fim']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'input-class',
                'placeholder': 'Digite o nome do livro'
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'textarea-class',
                'placeholder': 'Digite a descrição do livro',
                'rows': 4
            }),
            'autor': forms.Select(attrs={
                'class': 'select-class'
            }),
            'categoria': forms.Select(attrs={
                'class': 'select-class'
            }),
            'status': forms.Select(attrs={
                'class': 'select-class'
            }),
            'imagem': forms.ClearableFileInput(attrs={
                'class': 'file-input-class'
            }),
            'data_inicio': forms.DateInput(attrs={
                'type': 'date',
                'class': 'date-input-class'
            }),
            'data_fim': forms.DateInput(attrs={
                'type': 'date',
                'class': 'date-input-class'
            }),
        }