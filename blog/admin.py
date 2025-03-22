from django.contrib import admin
from blog.models import Category, CustomUser, Article, Comment

# Register your models here.
admin.site.register(Category)
admin.site.register(CustomUser)
admin.site.register(Article)
admin.site.register(Comment)
