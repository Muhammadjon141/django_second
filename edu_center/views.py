from django.shortcuts import render
from .models import Book, Authors, Comments, User

def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')


def books(request):
    books = Book.objects.all()
    comment = Comments.objects.all()
    user = User.objects.all()
    context = {'data_books': books,
               'data_comment': comment,
               'data_user': user}
    return render(request, 'books.html', context=context)

def authors(request):
    authors = Authors.objects.all()
    comment = Comments.objects.all()
    user = User.objects.all()
    context1 = {'data_authors': authors,
                'data_comment': comment,
                'data_user': user}
    return render(request, 'authors.html', context=context1)

def comments(request):
    comment = Comments.objects.all()
    user = User.objects.all()
    context2 = {'data_comment': comment,
                'data_user': user}
    return render(request, 'comments.html', context=context2)

def all(request):
    books = Book.objects.all()
    context = {'data_books': books}
    return render(request, 'all.html', context=context)