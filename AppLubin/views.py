# views.py
from django.shortcuts import render, redirect
from .forms import AuthorForm, BookForm, ReviewForm, BookSearchForm
from .models import Book, Author, Review

def home(request):
    books = Book.objects.all()  # Récupère tous les livres
    return render(request, 'AppLubin/home.html', {'books': books})

def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AuthorForm()
    return render(request, 'AppLubin/add_author.html', {'form': form})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm()
    return render(request, 'AppLubin/add_book.html', {'form': form})

def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ReviewForm()
    return render(request, 'AppLubin/add_review.html', {'form': form})

def search_books(request):
    form = BookSearchForm(request.GET)
    books = []
    if form.is_valid():
        title = form.cleaned_data.get('title')
        author = form.cleaned_data.get('author')
        if title or author:
            books = Book.objects.all()
            if title:
                books = books.filter(title__icontains=title)
            if author:
                books = books.filter(author__name__icontains=author)
    return render(request, 'AppLubin/search_books.html', {'form': form, 'books': books})
