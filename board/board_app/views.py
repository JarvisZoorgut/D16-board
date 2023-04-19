from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from datetime import datetime

from .forms import ArticleForm
from .models import Article, UserResponse


class ArticleCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('board_app.add_article')
    form_class = ArticleForm
    model = Article
    template_name = 'article_edit.html'

    def form_valid(self, form):
        article = form.save(commit=False)

class ArticleList(ListView):
    raise_exception = True
    model = Article
    ordering = 'articleTime'
    template_name = 'articles.html'
    context_object_name = 'articles'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        return context


class ArticleDetail(DetailView):
    raise_exception = True
    model = Article
    template_name = 'article.html'
    context_object_name = 'article'

class UserResponseList(ListView):
    raise_exception = True
    model = UserResponse
    ordering = 'responseTime'
    template_name = 'responses.html'
    context_object_name = 'responses'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        return context