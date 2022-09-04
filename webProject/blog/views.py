# Para mas info: https://youtu.be/UJfuqCefRxc
from django.shortcuts import render
from blog.models import Categoria, Post

# Create your views here.
def blog(request):
    posts = Post.objects.all()
    categoria = Categoria.objects.all()
    return render(request,"blog/blog.html", {"posts":posts, "categorias":categoria})

# Paginación - para mas info: https://youtu.be/ANHc7OgjLUo
def categoria(request, categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)
    posts=Post.objects.filter(categorias=categoria) # Apunta a categorias del modelo
    return render(request, "blog/categorias.html", {"posts":posts, 'categoria':categoria})