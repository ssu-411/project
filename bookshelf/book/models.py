from django.db import models
from django.utils.html import mark_safe
from django.core.files.storage import default_storage

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
    smallImage = models.ImageField(upload_to='books', default='books/None/no-imgs.jpg', blank=True)
    middleImage = models.ImageField(upload_to='books', default='books/None/no-imgm.jpg', blank=True)
    bigImage = models.ImageField(upload_to='books', default='books/None/no-imgl.jpg', blank=True)

    def smallImage_tag(self):
        if default_storage.exists(self.smallImage):
            return mark_safe('<img src="{:s}" />'.format(self.smallImage.url))
        else:
            return mark_safe('<img src="{:s}" />'.format("/media/books/None/no-imgs.jpg"))

    smallImage_tag.short_description = "Small Image"

    def middleImage_tag(self):
        if default_storage.exists(self.middleImage):
            return mark_safe('<img src="{:s}" />'.format(self.middleImage.url))
        else:
            return mark_safe('<img src="{:s}" />'.format("/media/books/None/no-imgm.jpg"))

    middleImage_tag.short_description = "Middle Image"

    def bigImage_tag(self):
        if default_storage.exists(self.bigImage):
            return mark_safe('<img src="{:s}" />'.format(self.bigImage.url))
        else:
            return mark_safe('<img src="{:s}" />'.format("/media/books/None/no-imgl.jpg"))

    bigImage_tag.short_description = "Big Image"

    def __str__(self):
        return self.title

    def get_authors(self):
        return ', '.join([x.name for x in self.author.iterator()])


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
