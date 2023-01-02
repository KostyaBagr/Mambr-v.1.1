from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from user_profile.models import MyUserProfile
from .models import *
class UserProfile(admin.ModelAdmin):
    list_display = ('id', 'username', 'email')
    list_display_links = ('id', 'username')
admin.site.register(MyUserProfile,UserProfile)