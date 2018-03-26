from django.contrib import admin
from .models import Publisher, Book, Author, Genre
from django.utils.html import mark_safe, format_html
from django.core.files.storage import default_storage

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('smallImage_display', 'title', 'rating',  )
    fields = ['title', 'author', 'rating', 'date', 'publisher', 'genre', ('smallImage_tag', 'middleImage_tag', 'bigImage_tag'),]
    readonly_fields = ['smallImage_tag', 'middleImage_tag', 'bigImage_tag', ]

    def smallImage_display(self, obj):
        if default_storage.exists(obj.smallImage):
            return mark_safe('<img src="{:s}" />'.format(obj.smallImage.url))
        else:
            return mark_safe('<img src="{:s}" />'.format("/media/books/None/no-imgs.jpg"))
    smallImage_display.short_description = "Book Cover"

admin.site.register(Book, BookAdmin)
admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Genre)
