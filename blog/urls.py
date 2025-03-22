from django.urls import path

from blog.views import *

urlpatterns = [
    path("", Index.as_view(), name="home"),
    path("news/category/<int:pk>/", ArticleByCategory.as_view(), name="category"),
    path("articles/<int:pk>/", ArticleDetail.as_view(), name="detail"),
    path("search/", ArticleSearch.as_view(), name="search"),
    path("delete/<int:pk>/", DeleteArticle.as_view(), name="delete"),
    path("add/", AddArticle.as_view(), name="add"),
    path("edit/<int:pk>/", EditArticle.as_view(), name="edit"),
    path("register/", user_register, name="register"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("add_comment/<int:pk>/", add_comment, name="comment"),
]