from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.
@login_required(login_url='/auth/login/')
def home(request):
    return render(request, 'home.html', { 'user': request.user })

@login_required(login_url='/auth/login/')
def signout(request):
    logout(request)
    return redirect('/auth/login/')