from django.shortcuts import render

def index(request):
    return render(request, "minha_estante/index.html")
