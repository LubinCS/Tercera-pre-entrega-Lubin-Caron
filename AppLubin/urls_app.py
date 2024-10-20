from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_author/', views.add_author, name='add_author'),
    path('add_book/', views.add_book, name='add_book'),
    path('add_review/', views.add_review, name='add_review'),
    path('search_books/', views.search_books, name='search_books'),
]