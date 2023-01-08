from django.template.backends import django
from user_profile.views import *
from django.urls import path
urlpatterns = [
    path('login/', MyLoginView.as_view(),name='login'),
    path('success/', success_login, name='success_login'),
    path('update_profile/',update_profile,name='update_profile'),
    path('registration/', SignUpView.as_view(),name='registration'),
    path('profile/',ProfilePage.as_view(), name='profile'),
    path('user_profile/<int:profile_pk>/', show_other_profiles, name='show_other_profiles'),
    path('log_out/',MyLogoutView.as_view(), name='log_out'),


    # path('edit_profile/',edit, name='edit')



]
