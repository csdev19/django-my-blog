from django.shortcuts import render
from django.views.generic import DetailView
from .models import Publication

# Create your views here.
class PublicationsView(DetailView):
    model = Publication

