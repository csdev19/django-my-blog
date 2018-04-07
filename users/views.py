from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
from .models import User

# Create your views here.
class UsersHome(TemplateView):
    template_name = 'users/home.html'

    def get_context_data (self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_detail'] = User.objects.all()
        return context

class UsersDetail(DetailView):
    model = User

class UsersShowAll(ListView):
    model = User
    template_name = 'users/show.html'
    # export object_list
