from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('borrowed/', views.borrowed_books, name='borrowed'),
    path('logout/', views.signout, name='logout')
]