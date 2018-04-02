from django.test import TestCase

# Create your tests here.
from book.models import Book, Author


class LinksTest(TestCase):
    def tests(self):
        Book(id=1, title='Title', rating=0.0).save()
        links = ['/admin/', '/register/', '/login/', '/', '/books', '/books/p0', '/book/1', '/book/2', '/user/1']
        codes = [200, 200, 200, 200, 200, 200, 200, 200, 404]
        for link, code in zip(links, codes):
            self.assertEqual(self.client.get(link, follow=True).status_code, code)
