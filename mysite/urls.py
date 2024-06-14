from django.urls import path
from .views import get_blogs, create_blog, get_blog, update_blog, update_title, delete_blog, delete_all

urlpatterns = [
    path('', get_blogs, name='home-page'),
    path('create/',create_blog),
    path('update/<str:id>', update_blog),
    path('patch/<str:id>', update_title),
    path('delete/<str:id>', delete_blog),
    path('delete/all', delete_all),
    path('<str:id>/',get_blog),
]
