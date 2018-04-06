from django.shortcuts import render
from django.views.generic import ListView
from .models import Comment

# Create your views here.
class Comments(ListView):
    model = Comment
    template_name = 'comments/comments.html'
