from django.urls import path
from bookshelf.registration.views import Register


urlpatterns = [
    path('', Register.as_view()),
]
