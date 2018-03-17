from django.db import models

# Create your models here.


class Book(models.Model):
    class Meta:
        db_table = 'Books'

    title = models.CharField(max_length=50)
    author = models.ManyToManyField('Author')
    rating = models.FloatField()
    date = models.PositiveIntegerField(null=True, blank=True)
    publisher = models.ForeignKey('Publisher', on_delete=models.SET_NULL, null=True, blank=True)
    genre = models.ManyToManyField('Genre', blank=True)
    smallImage = models.ImageField(upload_to='books', blank=True)
    bigImage = models.ImageField(upload_to='books', blank=True)

    def __str__(self):
        return self.title


class Publisher(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
