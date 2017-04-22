from django.contrib.auth.forms import AuthenticationForm

try:
    from django.contrib.auth import get_user_model

    User = get_user_model()
except ImportError:
    from django.contrib.auth.models import User
from django import forms
from .models import Comment, Post
from django.template.defaultfilters import slugify


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['description']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('description_comment', 'comment', 'commented_by')
