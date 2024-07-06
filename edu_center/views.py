from django.shortcuts import render
from .models import Book, Authors, Comments, User


books1 = Book.objects.all()
comment = Comments.objects.all()
user = User.objects.all()
authors1 = Authors.objects.all()
context = {'data_books': books1,
            'data_comment': comment,
            'data_user': user,
            'data_author': authors1}

def home(request):
    return render(request, 'home.html', context=context)

def login(request):
    return render(request, 'login.html', context=context)

def register(request):
    return render(request, 'register.html', context=context)

def books(request):
    return render(request, 'books.html', context=context)

def authors(request):
    return render(request, 'authors.html', context=context)

def comments(request):
    return render(request, 'comments.html', context=context)

def all(request):
    return render(request, 'all.html', context=context)