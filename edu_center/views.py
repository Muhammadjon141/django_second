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
    comments = Comments.objects.all()
    user = User.objects.all()
    context = {'data_books': books,
               'data_comment': comments,
               'data_user': user}
    return render(request, 'books.html', context=context)

def authors(request):
    authors = Authors.objects.all()
    authors = Authors.objects.all()
    comments = Comments.objects.all()
    user = User.objects.all()
    context1 = {'data_authors': authors,
                'data_comment': comments,
                'data_user': user}
    return render(request, 'authors.html', context=context1)

# Create your views here.
