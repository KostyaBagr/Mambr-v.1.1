from django.template.backends import django
from user_profile.views import *
from django.urls import path
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('login/', MyLoginView.as_view(),name='login'),
    path('success/', success_login, name='success_login'),
    path('update_profile/',update_profile,name='update_profile'),
    path('registration/', SignUpView.as_view(),name='registration'),
    path('profile/',ProfilePage.as_view(), name='profile'),
    path('user_profile/<int:profile_pk>/', show_other_profiles, name='show_other_profiles'),
    path('log_out/',MyLogoutView.as_view(), name='log_out'),
    path('reset_password/',  auth_views.PasswordResetView.as_view(template_name='user_profile/password_reset.html', email_template_name='user_profile/password_reset_email.html'), name='password_reset'),
    path('reset_password_sent/',  auth_views.PasswordResetDoneView.as_view(template_name='user_profile/reset_password_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/',  auth_views.PasswordResetConfirmView.as_view(template_name='user_profile/password_reset_form.html'), name='password_reset_confirm'),
    path('reset_password_complete/',  auth_views.PasswordResetCompleteView.as_view(template_name='user_profile/reset_password_complete.html'),name='password_reset_complete'),





]
