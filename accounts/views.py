from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('usr')
        password = request.POST.get('pwd')
        
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse('Incorrect username/password')

    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('usr')
        password = request.POST.get('pwd')

        obj = User.objects.create_user(username, email, password)
        obj.save()
        return redirect('login')

    return render(request, 'register.html')