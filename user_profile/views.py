from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.views.generic import ListView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.edit import FormMixin

from user_profile.forms import *
# Create your views here.
from user_profile.models import *
from django.contrib.auth.views import LogoutView

def success_login(request):
    dict = {
        'title':'Успешный вход в аккаунт'
    }

    return render(request, 'user_profile/login_is_okay.html',dict)


class SuccessMessageMixin:
    @property
    def success_msg(self):
        return False

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super().form_valid(form)



class MyLoginView(LoginView):
    template_name = 'user_profile/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('success_login')

    def get_success_url(self):
        return self.success_url



class MyRegistrationView(CreateView):
    model = User
    template_name = 'user_profile/register_form.html'
    form_class = UserRegistrationForm
    success_msg ='Регистриция прошла успешно'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        email = form.cleaned_data['email']
        aut_user = authenticate(username=username, password=password,email=email)
        login(self.request, aut_user)
        return form_valid


#
def get_profile(request):
    dict = {
        'title': 'Ваш профиль'
    }
    return render(request, 'user_profile/user_page.html', dict)
#
#
class MyLogoutView(LogoutView):
    next_page = reverse_lazy('home')






