from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from blog.models import Article, CustomUser, Comment


class RegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "class":"form-control",
        "placeholder":"Your Email"
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class":"form-control",
        "placeholder":"Your Username"
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class":"form-control",
        "placeholder":"Your Password"
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class":"form-control",
        "placeholder":"Again Password"
    }))

    class Meta:
        model = CustomUser
        fields = ["email","username","password1","password2"]

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class":"form-control",
        "placeholder":"Username"
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class":"form-control",
        "placeholder":"Password"
    }))

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title","info","photo","category"]
        widgets = {
            'title':forms.TextInput(attrs={
                'class':"form-control",
                'placeholder':"title"
            }),
            'info': forms.Textarea(attrs={
                'class': "form-control",
                'placeholder': "Description"
            }),
            'photo': forms.FileInput(),
            'category':forms.Select(attrs={
                'class': "form-control"
            })
        }


class CommentForm(forms.ModelForm):
        class Meta:
            model = Comment
            fields = ("title",)
            widgets = {
                "title": forms.Textarea(attrs={
                    "class":"form-control",
                    "rows":3
                })
            }