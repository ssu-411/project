from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import PasswordChangeView, login
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import UserCreationForm

from registration.models import MyUser
from .forms import MyUserRegisterForm, UserRegisterForm, PasswordChangeCustomForm, AuthForm
from django.views.decorators.csrf import csrf_protect
from django.views.generic import CreateView, FormView


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
            login(self.request, user)
            return redirect('/')
        else:
            return render(request, 'signup.html', {
                'form': form,
                'form2': form2,
                'form3': form3
            })


class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'user.html'
    form_class = PasswordChangeCustomForm
    extra_context = {"changed": False}

    def get_context_data(self, **kwargs):
        user_id = int(self.request.get_raw_uri().split('user/')[1].split('/')[0])
        if self.request.user.id == user_id:
            context = super().get_context_data(**kwargs)
        else:
            context = {}
        context['profile'] = MyUser.objects.get(user=User.objects.get(id=user_id))
        self.extra_context['changed'] = False
        return context

    def get_success_url(self):
        self.extra_context['changed'] = True
        user_id = self.request.get_raw_uri().split('user/')[1].split('/')[0]
        return '/user/{}'.format(user_id)


class Login(FormView):
    form_class = AuthForm

    @method_decorator(csrf_protect)
    def get(self, request, *args, **kwargs):
        data = {
            'form': self.form_class(initial={'prev_page': '/'}),
        }
        return render(request, self.template_name, data)

    @method_decorator(csrf_protect)
    def post(self, request, *args, **kwargs):
        prev_page = request.POST.get('prev_page')
        if not prev_page:
            prev_page = request.META.get('HTTP_REFERER', '/')
        data = dict(request.POST.items())
        data['prev_page'] = prev_page
        form = self.form_class(data)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect(prev_page)
            else:
                form.add_error(None, "Неправильный логин и/или пароль")
        return render(request, 'login.html', {
            'form': form
        })
