from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("autor/novo/", views.criar_autor, name="criar_autor"),
    path("categoria/nova/", views.criar_categoria, name="criar_categoria"),
    path("post/novo/", views.criar_post, name="criar_post"),
    path("buscar/", views.buscar_posts, name="buscar_posts"),
]
