from django.shortcuts import render
from .models import Book, Authors

def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def books(request):
    books = Book.objects.all()
    context = {'data_books': books}
    return render(request, 'books.html', context=context)

def authors(request):
    authors = Authors.objects.all()
    context1 = {'data_authors': authors}
    return render(request, 'authors.html', context=context1)

# Create your views here.
