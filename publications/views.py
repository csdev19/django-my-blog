from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from .models import Publication

# Create your views here.
class PublicationsView(ListView):
    model = Publication
    template_name = 'publications/publications.html'

class PublicationsDetail(DetailView):
    model = Publication
    template_name = 'publications/public_detail.html'
