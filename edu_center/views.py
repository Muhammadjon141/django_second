from django.shortcuts import render, redirect
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
    return render(request, 'home.html')

def login(request):
    if request.method == "POST":
        print("dgsbbbfbfgbbbbbbbbbbbbbbbbbbbbb", request.POST)
    return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['user_name']
        password = request.POST['password']
        password2 = request.POST['password1']
        new_user = User(first_name=first_name, last_name=last_name, email=email, username=username)
        new_user.set_password(password)
        new_user.save()
        return redirect('login')
    

    return render(request, 'register.html')

def books(request):
    return render(request, 'books.html', context=context)

def authors(request):
    return render(request, 'authors.html')

def comments(request):
    return render(request, 'comments.html')

def all(request):
    return render(request, 'all.html')