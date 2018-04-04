from django.urls import path
from .views import UsersHome, UsersShowAll, UsersDetail

app_name = 'users'

urlpatterns = [
    path('home', UsersHome.as_view(), name='home'),
    path('<pk>/', UsersDetail.as_view(), name='user_detail'),
    path('all', UsersShowAll.as_view(), name='all')
]