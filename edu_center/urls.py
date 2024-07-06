from django.urls import path
from .views import home, login, register, books, authors, comments,all

urlpatterns = [
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('books/', books, name='books'),
    path('authors/', authors, name='authors'),
    path('comments/', comments, name='comments'),
]