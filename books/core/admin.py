from django.contrib.admin.options import ModelAdmin

from books.core.models import Author, Book
from books.core.forms import BookForm
from books.sites import booksite

class BookModelAdmin(ModelAdmin):
    form = BookForm

booksite.register(Author, ModelAdmin)
booksite.register(Book, BookModelAdmin)
