from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.tokens import default_token_generator

from django.contrib.auth.views import LoginView, PasswordContextMixin
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.views.generic import ListView, TemplateView, FormView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from user_profile.forms import *
# Create your views here.
from user_profile.models import *
from django.contrib.auth.views import LogoutView


def success_login(request):
    dict = {
        'title': 'Успешный вход в аккаунт'
    }

    return render(request, 'user_profile/login_is_okay.html', dict)


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
    context_object_name ='form'

    def get_success_url(self):
        return self.success_url




class SignUpView(CreateView):
    form_class = CreateUserProfile
    success_url = reverse_lazy('home')
    template_name = 'user_profile/register_form.html'
    def form_valid(self, form):

        form_valid = super().form_valid(form)

        username = form.cleaned_data["username"]
        email = form.cleaned_data['email']
        password = self.request.POST['password1']

        aut_user = authenticate(username=username, password=password, email=email)
        login(self.request, aut_user)
        return form_valid




def update_profile(request):
    user = request.user
    form = CustomUserProfile(instance=user)
    msg = False
    if request.method == 'POST':
        form = CustomUserProfile(request.POST,request.FILES, instance=user)
        form.save()
        # return redirect('profile')
        msg =True
    dict = {
        'msg':msg,
        'form':form,
        'title': "Редактирование профиля"
    }
    return render(request, 'user_profile/user_settings.html', dict)


def show_other_profiles(request, profile_pk):
    get_profile = MyUserProfile.objects.get(pk=profile_pk)

    dict={
        'show_user':get_profile
    }
    return render(request,'user_profile/show_user.html', dict)


class ProfilePage(ListView):
    template_name = 'user_profile/user_page.html'
    model = MyUserProfile
    pk_url_kwarg = 'profile_pk'
    context_object_name = 'get_user'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated == True:
            if request.method.lower() in self.http_method_names:
                handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
            else:
                handler = self.http_method_not_allowed
            return handler(request, *args, **kwargs)
        else:
            return redirect("login")



#
#
class MyLogoutView(LogoutView):
    next_page = reverse_lazy('home')

