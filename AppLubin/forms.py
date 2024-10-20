from django import forms
from .models import Author, Book, Review

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'bio']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_date']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['book', 'reviewer_name', 'content', 'rating']

class BookSearchForm(forms.Form):
    title = forms.CharField(required=False)
    author = forms.CharField(required=False)