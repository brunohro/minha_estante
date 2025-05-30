"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from minha_estante.views import index, cadastrar_livro, editar_livro, deletar_livro, login_view, logout_view, cadastrar_usuario, adm

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name='index'),
    path("cadastrar_livro/", cadastrar_livro, name="cadastrar_livro"),
    path("editar_livro/<int:id>", editar_livro, name="editar_livro"),
    path("deletar_livro/<int:id>", deletar_livro, name="deletar_livro"),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('cadastrar_usuario/', cadastrar_usuario, name='cadastrar_usuario'),
    path('adm/', adm, name="adm"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
