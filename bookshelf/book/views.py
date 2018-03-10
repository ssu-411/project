from django.template import Library
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import TemplateView

# Create your views here.

from book.models import Book

BooksOnPage = 5
register = Library()


@register.tag
def prev_page(value):
    return value - 1


class BooksView(TemplateView):
    template_name = "books.html"

    def get_context_data(self, page=0, **kwargs):
        context = super().get_context_data(**kwargs)
        page = int(page)
        context['page'] = page
        context['prev_page'] = str(page - 1)
        start = page * BooksOnPage
        context['books'] = Book.objects.all()[start:start + BooksOnPage]
        if len(Book.objects.all()) > page + BooksOnPage:
            context['next_page'] = page + 1
        return context


class BookView(TemplateView):
    def get_context_data(self, id=None, **kwargs):
        context = super().get_context_data(**kwargs)
        self.template_name = "book.html"
        try:
            book = Book.objects.get(id=id)
            context['book'] = book
        except ObjectDoesNotExist:
            context['id'] = id
            self.template_name = "book not found.html"
        return context
