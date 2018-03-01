from django.db import models

# Create your models here.


class Book(models.Model):
    class Meta:
        db_table = 'Books'

    title = models.CharField(max_length=50)
    author = models.ManyToManyField('Author')
    rating = models.FloatField()
    date = models.DateField()
    publisher = models.ForeignKey('Publisher', on_delete=models.SET_NULL, null=True)
    genre = models.ManyToManyField('Genre')

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
