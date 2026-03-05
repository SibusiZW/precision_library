from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import BookForm
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
    if request.method == 'POST':
        form = BookForm(request.POST)

        if form.is_valid():
            form.save()
    else:
        form = BookForm()

    return render(request, 'add_book.html', { 'form': form })

@login_required(login_url='/auth/login/')
def delete_book(request, pk):
    obj = Book.objects.get(pk=pk)
    obj.delete()

    return redirect('home')

@login_required(login_url='/auth/login/')
def signout(request):
    logout(request)
    return redirect('/auth/login/')