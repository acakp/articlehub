from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Article
from .forms import ArticleForm


class ArticleListView(ListView):
    model = Article
    template_name = "articles_app/article_list.html"
    context_object_name = "articles"
    paginate_by = 10


class ArticleDetailView(DetailView):
    model = Article
    template_name = "articles_app/article_detail.html"
    context_object_name = "article"


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    form_class = ArticleForm
    template_name = "articles_app/article_form.html"
    success_url = reverse_lazy("article_list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = "articles_app/article_form.html"
    success_url = reverse_lazy("article_list")

    def get_queryset(self):
        return Article.objects.filter(author=self.request.user)
