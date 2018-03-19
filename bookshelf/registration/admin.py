from django.contrib import admin
from .models import MyUser, BookRating

# Register your models here.

admin.site.register(MyUser)
admin.site.register(BookRating)
