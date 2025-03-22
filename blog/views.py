from django.contrib.auth import login, logout
from django.db.models import Q
from django.template.defaulttags import comment
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect

from blog.forms import ArticleForm, RegisterForm, LoginForm, CommentForm
from blog.models import Article, Comment

class Index(ListView):
    model = Article
    context_object_name = "articles"
    template_name = "blog/index.html"

class ArticleByCategory(Index):
    def get_queryset(self):
        return Article.objects.filter(category_id=self.kwargs['pk'])

class ArticleDetail(DetailView):
    model = Article
    context_object_name = "article"
    template_name = "blog/detail.html"
    form_class = CommentForm

    def get_queryset(self):
        return Article.objects.filter(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        article = Article.objects.get(pk=self.kwargs['pk'])
        context['comments'] = Comment.objects.filter(article=article).order_by('-created_at')
        context['comment_form'] = CommentForm()
        return context

class ArticleSearch(Index):
    def get_queryset(self):
        word = self.request.GET.get('q')
        articles = Article.objects.filter(Q(title__icontains=word))
        return articles

# def add_article(request):
#     if request.method == "POST":
#         form = ArticleForm(data=request.POST)
#         if form.is_valid():
#             article = form.save(commit=False)
#             article.user = request.user
#             article.save()
#             return redirect("home")
#     else:
#         form = ArticleForm()
#     context = {
#         "form":form
#     }
#     return render(request,"blog/article.html",context)

class AddArticle(CreateView):
    model = Article
    template_name = "blog/article.html"
    form_class = ArticleForm
#
class EditArticle(UpdateView):
    model = Article
    template_name = "blog/article.html"
    form_class = ArticleForm


class DeleteArticle(DeleteView):
    model = Article
    success_url = reverse_lazy("home")
    context_object_name = "article"

def user_register(request):
    if request.method == "POST":
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("login")
    else:
        form = RegisterForm()
    context = {
        "title":"Register",
        "form":form
    }
    return render(request,"blog/register.html", context)

def user_login(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect("home")
    else:
        form = LoginForm()
    context = {
        "title":"Login",
        "form":form
    }
    return render(request,"blog/login.html", context)

def user_logout(request):
    logout(request)
    return redirect("login")

def add_comment(request,pk):
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.article = Article.objects.get(pk=pk)
        comment.save()
    else:
        pass
    return redirect("detail",pk)