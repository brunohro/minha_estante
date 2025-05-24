from django.contrib import admin
from .models import Autores, Categoria, Livro

@admin.register(Autores)
class AutoresAdmin(admin.ModelAdmin):
    list_display = ('nome',)

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', )

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('nome', )