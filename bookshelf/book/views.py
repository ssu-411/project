from django.db.models import Q
from django.template import Library
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import TemplateView

# Create your views here.

from book.models import Book

ROWS_NUM = 5
BOOKS_IN_ROW = 5
BOOKS_ON_PAGE = ROWS_NUM * BOOKS_IN_ROW
register = Library()


@register.tag
def prev_page(value):
    return value - 1


class BooksView(TemplateView):
    template_name = "books.html"

    def get_context_data(self, page=0, *args, **kwargs):
        query = self.request.GET.get('q', '').strip()
        if query:
            book_qs = Book.objects.filter(
                Q(title__icontains=query) |
                Q(author__name__icontains=query) |
                Q(genre__name__icontains=query)
            ).distinct()
        else:
            book_qs = Book.objects.all()
        context = super().get_context_data(**kwargs)
        page = min(int(page), book_qs.count() // BOOKS_ON_PAGE)
        context['page'] = page
        context['prev_page'] = str(page - 1)
        start = page * BOOKS_ON_PAGE
        books = book_qs[start:start + BOOKS_ON_PAGE]

        context['books'] = [books[x * BOOKS_IN_ROW: x * BOOKS_IN_ROW + BOOKS_IN_ROW] for x in range(ROWS_NUM)]
        if book_qs.count() > start + BOOKS_ON_PAGE:
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
