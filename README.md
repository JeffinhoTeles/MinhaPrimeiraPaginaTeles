# SuaPrimeiraPaginaTeles

Projeto Web desenvolvido em **Django** seguindo o padrão **MVT (Model - View - Template)**.

Este projeto foi criado como prática para aprender a estrutura básica de uma aplicação web em Django, utilizando:

✅ Herança de templates  
✅ Models (3 classes)  
✅ Formulários para inserir dados  
✅ Formulário de busca no banco de dados  

---

## ✅ Tecnologias utilizadas

- Python
- Django
- HTML (Templates do Django)
- SQLite (banco padrão do Django)

---

## ✅ Requisitos atendidos

### ✅ 1) Herança de templates
Foi criada uma estrutura base utilizando um template principal:

📌 `blog/templates/blog/base.html`

As páginas estendem este template com:

```html
{% extends "blog/base.html" %}
```

---

### ✅ 2) Pelo menos 3 classes em models
As classes foram criadas no arquivo:

📌 `blog/models.py`

Models criados:
- `Autor`
- `Categoria`
- `Post`

---

### ✅ 3) Um formulário para inserir dados em cada model
Foi criado um formulário para cada model no arquivo:

📌 `blog/forms.py`

Forms:
- `AutorForm`
- `CategoriaForm`
- `PostForm`

---

### ✅ 4) Um formulário para buscar algo no BD
Foi criado um formulário de busca no arquivo:

📌 `blog/forms.py`

Form:
- `BuscaPostForm`

Busca feita no banco por título do post usando:

```python
Post.objects.filter(titulo__icontains=termo)
```

---

## 🚀 Como rodar o projeto

### ✅ 1) Clonar o repositório (caso esteja no GitHub)

```bash
git clone https://github.com/SEU_USUARIO/SuaPrimeiraPaginaTeles.git
cd SuaPrimeiraPaginaTeles
```

---

### ✅ 2) Criar e ativar o ambiente virtual

Criar o ambiente virtual:

```bash
python -m venv venv
```

Ativar no PowerShell (Windows):

```bash
venv\Scripts\Activate.ps1
```

Ativar no CMD:

```bash
venv\Scripts\activate
```

✅ Se ativou corretamente, vai aparecer:

```bash
(venv)
```

---

### ✅ 3) Instalar dependências

```bash
pip install -r requirements.txt
```

---

### ✅ 4) Rodar migrações do banco

```bash
python manage.py migrate
```

---

### ✅ 5) Rodar o servidor

```bash
python manage.py runserver
```

Abrir no navegador:

📌 http://127.0.0.1:8000/

---

## ✅ Ordem recomendada para testar (IMPORTANTE)

### ✅ 1) Home (lista posts cadastrados)
- http://127.0.0.1:8000/

---

### ✅ 2) Cadastrar Autor
📌 Formulário para inserir um autor no banco

- http://127.0.0.1:8000/autor/novo/

---

### ✅ 3) Cadastrar Categoria
📌 Formulário para inserir uma categoria no banco

- http://127.0.0.1:8000/categoria/nova/

---

### ✅ 4) Cadastrar Post
📌 Formulário para inserir post e relacionar autor/categoria

- http://127.0.0.1:8000/post/novo/

---

### ✅ 5) Buscar Posts pelo título
📌 Busca no banco utilizando um termo digitado

- http://127.0.0.1:8000/buscar/

---

## 🛠️ Admin Django (opcional)

Criar superusuário:

```bash
python manage.py createsuperuser
```

Acessar admin:

📌 http://127.0.0.1:8000/admin/

---

## 📁 Estrutura principal do projeto

```
SuaPrimeiraPaginaTeles/
│
├── manage.py
├── requirements.txt
├── README.md
│
├── core/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
└── blog/
    ├── models.py
    ├── views.py
    ├── forms.py
    ├── urls.py
    ├── admin.py
    └── templates/
        └── blog/
            ├── base.html
            ├── home.html
            ├── autor_form.html
            ├── categoria_form.html
            ├── post_form.html
            └── busca.html
```

---

## ✅ Observações finais

- O projeto utiliza SQLite por padrão (já incluso no Django).
- Os formulários possuem CSRF Token para segurança.
- A navegação entre páginas foi feita via menu no `base.html`.

✅ Projeto pronto para entrega 🚀🔥
