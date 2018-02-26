from django.urls import path
from Bookshelf.registration.views import Register


urlpatterns = [
    path('', Register.as_view()),
]
