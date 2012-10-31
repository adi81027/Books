from django.contrib.admin.widgets import RelatedFieldWidgetWrapper
from django import forms

from books.core.models import Book
from books.sites import booksite


class BookForm(forms.ModelForm):
    author = Book._meta.get_field('author').formfield(
        widget=RelatedFieldWidgetWrapper(
            Book._meta.get_field('author').formfield().widget,
            Book._meta.get_field('author').rel,
            booksite,
            can_add_related=True
        )
    )

    class Meta:
        model = Book
