from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_protect
from django.views.generic import CreateView
# Create your views here.


class Register(CreateView):
    form_class = UserCreationForm

    @method_decorator(csrf_protect)
    def get(self, request, *args, **kwargs):
        return render(request, 'signup.html', {'form': self.form_class})

    @method_decorator(csrf_protect)
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form.clean()
            return render(request, 'signup.html', {'form': form})
