from django.urls import path
from .views import Comments

app_name = 'comments'

urlpatterns = [
    path('', Comments.as_view(), name='all')
]