from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Book

# Create your views here.
@login_required(login_url='/auth/login/')
def home(request):
    books = Book.objects.all().order_by('name')
    count = books.count()
    return render(request, 'home.html', { 'user': request.user, 'books': books, 'count': count })

@login_required(login_url='/auth/login/')
def borrowed_books(request):
    books = Book.objects.filter(status='Borrowed').order_by('name')
    count = books.count()

    return render(request, 'borrowed.html', { 'books': books, 'count': count })

@login_required(login_url='/auth/login/')
def add_book(request):
    return render(request, 'add_book.html')

@login_required(login_url='/auth/login/')
def signout(request):
    logout(request)
    return redirect('/auth/login/')