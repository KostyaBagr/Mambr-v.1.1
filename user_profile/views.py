from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.edit import FormMixin, UpdateView
# from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
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


# @login_required
# def edit(request):
#     if request.method == 'POST':
#         user_form = UserEditForm(instance=request.user, data=request.POST)
#         profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#     else:
#         user_form = UserEditForm(instance=request.user)
#         profile_form = ProfileEditForm(instance=request.user.profile)
#         return render(request,
#                       'user_profile/edit.html',
#                       {'user_form': user_form,
#                        'profile_form': profile_form})
class MyLoginView(LoginView):
    template_name = 'user_profile/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('success_login')

    def get_success_url(self):
        return self.success_url


class SignUpView(CreateView):
    form_class = CreateUserProfile
    success_url = reverse_lazy('home')
    template_name = 'user_profile/register_form.html'

    def post(self, request, *args, **kwargs):
        form = self.get_form(CreateUserProfile)
        # form = CreateUserProfile(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data["username"]
        email = form.cleaned_data['email']
        password = self.request.POST['password1']
        # password2 = form.cleaned_data['password2']
        aut_user = authenticate(username=username, password=password, email=email)
        login(self.request, aut_user)
        return form_valid



# class ProfileUpdateView(LoginRequiredMixin,UpdateView):
#     model = MyUserProfile
#     template_name = 'user_profile/edit.html'
#     form_class = CreateUserProfile
#     success_url = reverse_lazy('home')
#     context_object_name = 'form'
#     success_msg = 'Запись успешно обновлена'
#
#     def get_context_data(self, **kwargs):
#         kwargs['update_button'] = True
#         return super().get_context_data(**kwargs)
#
#     def get_form_kwargs(self):
#         """Return the keyword arguments for instantiating the form."""
#         kwargs = super().get_form_kwargs()
#         return kwargs
# class MyRegistrationView(CreateView):
#     model = MyUserProfile
#     template_name = 'user_profile/register_form.html'
#     form_class =  CreateUserProfile
#     success_msg ='Регистриция прошла успешно'
#     success_url = reverse_lazy('home')
#
#     def form_valid(self, form):
#         form_valid = super().form_valid(form)
#         name = form.cleaned_data["name"]
#         password = form.cleaned_data["password"]
#         email = form.cleaned_data['email']
#         aut_user = authenticate(name=name, password=password,email=email)
#         login(self.request, aut_user)
#         return form_valid


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
