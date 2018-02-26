from django.urls import path
from registration.views import Register


urlpatterns = [
    path('', Register.as_view()),
]
