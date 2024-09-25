from django import forms
from .models import Book

class BorrowForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('borrower', 'due_date')