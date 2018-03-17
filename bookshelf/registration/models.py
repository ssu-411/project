from django.db import models
from django.contrib.auth.models import User

# Create your models here.

genders = (
    ('M', 'Мужской'),
    ('F', 'Женский')
)


class MyUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    already_read = models.ManyToManyField('book.Book', blank=True)
    gender = models.CharField(max_length=10, choices=genders)
    age = models.PositiveSmallIntegerField()
    favorite_genres = models.ManyToManyField('book.Genre', blank=True)
    favorite_author = models.ManyToManyField('book.Author', blank=True)

    def __str__(self):
        return self.user.username
