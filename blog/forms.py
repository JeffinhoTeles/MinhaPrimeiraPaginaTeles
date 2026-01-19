from django import forms
from .models import Autor, Categoria, Post


class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ["nome", "email"]


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ["titulo"]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["titulo", "conteudo", "autor", "categoria"]


class BuscaPostForm(forms.Form):
    termo = forms.CharField(label="Buscar Post por título", max_length=120, required=False)
