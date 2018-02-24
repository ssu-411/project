from django.shortcuts import render
from django.contrib import auth


def general(request):
    args = {'user': auth.get_user(request).username}
    return render(request, 'main.html', args)
