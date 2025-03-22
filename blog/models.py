from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

from config import settings


# Create your models here.

class CustomUser(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)


class Category(models.Model):
    title = models.CharField(max_length=250, unique=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title

class Article(models.Model):
    title = models.CharField(max_length=250, unique=True)
    info = models.TextField(blank=True)
    photo = models.ImageField(upload_to="articles/", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    def get_photo(self):
        try:
            return self.photo.url
        except:
            return "https://thumb.ac-illust.com/b1/b170870007dfa419295d949814474ab2_t.jpeg"

    def get_absolute_url(self):
        return reverse("home")

    def __str__(self):
        return self.title

class Comment(models.Model):
    title = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
