from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('borrowed/', views.borrowed_books, name='borrowed'),
    path('add/', views.add_book, name='add'),
    path('delete/<int:pk>/', views.delete_book, name='delete'),
    path('edit/<int:pk>/', views.edit_book, name='edit'),
    path('logout/', views.signout, name='logout')
]