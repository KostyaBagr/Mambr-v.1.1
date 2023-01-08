from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, TemplateView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.edit import FormMixin, UpdateView
# from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from user_profile.forms import *
# Create your views here.
from user_profile.models import *
from django.contrib.auth.views import LogoutView
from user_profile.decorators import  allowed_users

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
            return HttpResponse("Уберите пробел")

    def form_valid(self, form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data["username"]
        email = form.cleaned_data['email']
        password = self.request.POST['password1']
        # password2 = form.cleaned_data['password2']
        aut_user = authenticate(username=username,password=password, email=email)
        login(self.request, aut_user)
        return form_valid



def update_profile(request):
    user = request.user
    form = CustomUserProfile(instance=user)
    if request.method == 'POST':

        form = CustomUserProfile(request.POST,request.FILES, instance=user)
        form.save()
        return redirect('profile')



    dict = {
        'form':form
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
