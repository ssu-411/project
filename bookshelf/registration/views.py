from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import UserCreationForm
from .forms import MyUserRegisterForm, UserRegisterForm
from django.views.decorators.csrf import csrf_protect
from django.views.generic import CreateView
# Create your views here.


class Register(CreateView):
    form_class = UserCreationForm
    form2 = MyUserRegisterForm
    form3 = UserRegisterForm

    def fun(self):
        return {'form': self.form_class,
                'form2': self.form2,
                'form3': self.form3}

    @method_decorator(csrf_protect)
    def get(self, request, *args, **kwargs):
        return render(request, 'signup.html', self.fun())

    @method_decorator(csrf_protect)
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        form2 = self.form2(request.POST)
        form3 = self.form3(request.POST)
        if form.is_valid() and form2.is_valid() and form3.is_valid():
            user = form.save(commit=False)
            user2 = form3.save(commit=False)
            my_user = form2.save(commit=False)
            user.email = user2.email
            user.first_name = user2.first_name
            user.last_name = user2.last_name
            user.save()

            my_user.user = user
            my_user.save()
            return redirect('/')
        else:
            form.clean()
            form2.clean()
            form3.clean()
            return render(request, 'signup.html', self.fun())
