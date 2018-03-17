from django.db import models
from django.contrib.auth.models import User

# Create your models here.

genders = (
    ('M', 'Мужской'),
    ('F', 'Женский')
)


class MyUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    to_read = models.ManyToManyField('book.Book', blank=True)
    gender = models.CharField(max_length=10, choices=genders)
    age = models.PositiveSmallIntegerField()
    favorite_genres = models.ManyToManyField('book.Genre', blank=True)
    favorite_author = models.ManyToManyField('book.Author', blank=True)
    rated_books = models.ManyToManyField('BookRating', blank=True)

    def __str__(self):
        return self.user.username

class BookRating(models.Model):
    rating = models.PositiveSmallIntegerField()
    rtd_book = models.ForeignKey('book.Book', on_delete=models.PROTECT, null=False)

    def __str__(self):
        return "{:20s} -> {:d}".format(self.rtd_book.title, self.rating)
