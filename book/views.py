from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def books(request):
    return render(request, 'books.html')

def authors(request):
    return render(request, 'authors.html')

# Create your views here.
