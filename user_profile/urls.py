from django.template.backends import django
from user_profile.views import *
from django.urls import path
urlpatterns = [
    path('login/', MyLoginView.as_view(),name='login'),
    path('success/', success_login, name='success_login'),
    # path('edit_profile/', get_profile, name='edit_profile'),
    # path('login/', get_login, name='login'),
    # # path('update_profile', update_profile, name='update_profile'),
    # path('registration/', MyRegistrationView.as_view(), name='registration'),
    path('registration/', SignUpView.as_view(),name='registration'),
    path('profile/',get_profile, name='profile'),
    path('log_out/',MyLogoutView.as_view(), name='log_out'),

    # path('edit_profile/',edit, name='edit')



]
