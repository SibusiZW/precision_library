from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Book

# Create your views here.
@login_required(login_url='/auth/login/')
def home(request):
    books = Book.objects.all()
    return render(request, 'home.html', { 'user': request.user, 'books': books })

@login_required(login_url='/auth/login/')
def signout(request):
    logout(request)
    return redirect('/auth/login/')