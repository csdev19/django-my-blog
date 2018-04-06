from django.urls import path, include
from .views import PublicationsView, PublicationsDetail

app_name = 'publications'

urlpatterns = [
    path('', PublicationsView.as_view(), name='home'),
    path('<int:pk>/', PublicationsDetail.as_view(), name='detail'),
]