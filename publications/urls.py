from django.urls import path, include
from .views import PublicationsView

app_name = 'publications'

urlpatterns = [
    path('', PublicationsView.as_view(), name='view')
]