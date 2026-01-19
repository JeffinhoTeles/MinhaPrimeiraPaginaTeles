from django.shortcuts import render, redirect
from .models import Post
from .forms import AutorForm, CategoriaForm, PostForm, BuscaPostForm


def home(request):
    posts = Post.objects.all().order_by("-criado_em")
    return render(request, "blog/home.html", {"posts": posts})


def criar_autor(request):
    if request.method == "POST":
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = AutorForm()

    return render(request, "blog/autor_form.html", {"form": form})


def criar_categoria(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = CategoriaForm()

    return render(request, "blog/categoria_form.html", {"form": form})


def criar_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = PostForm()

    return render(request, "blog/post_form.html", {"form": form})


def buscar_posts(request):
    form = BuscaPostForm(request.GET)
    posts = []

    if form.is_valid():
        termo = form.cleaned_data.get("termo")
        if termo:
            posts = Post.objects.filter(titulo__icontains=termo).order_by("-criado_em")

    return render(request, "blog/busca.html", {"form": form, "posts": posts})
