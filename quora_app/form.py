
from .models import Comment
from django import forms
from django.contrib import admin
from .models import Post



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'upload']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']