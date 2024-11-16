from django.shortcuts import render, redirect
from .models import Article  # --- 1
from .forms import ArticleForm
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView
)
"""
#def index(request):
    articles = Article.objects.all()  # --- 2
    params = {  # --- 3
        'articles': articles,
    }
    return render(request, 'blog/index.html', params)  # --- 4
"""
class ArticleList(ListView):
    model = Article
    template_name = "blog/index.html"
    context_object_name = 'articles'
'''
def create(request):
    if request.method == 'POST':
        obj = Article()  # 1
        form = ArticleForm(request.POST, instance=obj)  # 2
        if form.is_valid():  # Validar el formulario antes de guardar
            form.save()  # 3
            return redirect('index')
    else:
        form = ArticleForm()  # Crear una instancia del formulario vacío
    
    return render(request, 'blog/create.html', {'form': form})
'''

class ArticleCreate(CreateView):
    model = Article
    template_name = 'blog/create.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('index')
"""

def detail(request, article_id):  # --- 1
    article = Article.objects.get(id=article_id)  # --- 2
    params = {
        'article': article,  # Pasamos el artículo al contexto para la plantilla
    }
    return render(request, 'blog/detail.html', params)  # Renderizamos la plantilla 'detail.html'
"""

class ArticleDetail(DetailView):
    model = Article
    template_name = "blog/detail.html"
    context_object_name = 'article'
    pk_url_kwarg = 'article_id'

'''   
def edit(request, article_id):
    article = Article.objects.get(id=article_id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():  # Asegurarse de que el formulario es válido antes de guardar
            form.save()
        return redirect('detail', article_id)
    else:
        params = {
            'article': article,
            'form': ArticleForm(instance=article),
        }
        return render(request, 'blog/edit.html', params)
   # Renderizar la plantilla para editar
'''

class ArticleUpdate(UpdateView):
    model = Article
    fields = '__all__'
    template_name = 'blog/edit.html'
    pk_url_kwarg = 'article_id'

def get_success_url(self):
    return reverse('detail', kwargs={'article_id': self.object.pk})

'''
def delete(request, article_id):
    article = Article.objects.get(id=article_id)
    
    if request.method == 'POST':
        article.delete()
        return redirect('index')
    else:
        params = {
            'article': article,
        }
        return render(request, 'blog/delete.html', params)
'''

class ArticleDelete(DeleteView):
    model = Article
    fields = '__all__'
    template_name = 'blog/edit.html'
    pk_url_kwarg = 'article_id'