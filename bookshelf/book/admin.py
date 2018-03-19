from django.contrib import admin
from .models import Publisher, Book, Author, Genre
from django.utils.html import mark_safe, format_html

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('smallImage_display', 'title', 'rating',  )
    fields = ['title', 'author', 'rating', 'date', 'publisher', 'genre', ('smallImage_tag', 'middleImage_tag', 'bigImage_tag'),]
    readonly_fields = ['smallImage_tag', 'middleImage_tag', 'bigImage_tag', ]

    def smallImage_display(self, obj):
        return mark_safe('<img src="{:s}" />'.format(obj.smallImage.url))
    smallImage_display.short_description = "Book Cover"

admin.site.register(Book, BookAdmin)
admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Genre)
