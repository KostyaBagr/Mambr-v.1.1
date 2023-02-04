from django.contrib import admin
from .models import *
# Register your models here.
from django import forms



from blog.models import Questions



class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'q_name', 'time_create', 'is_published')
    list_display_links = ('id', 'q_name')
    search_fields = ('q_name', 'id')
    list_editable = ('is_published',)

    list_filter = ('q_name', 'time_create')


# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name')
#     list_display_links = ('id', 'name')
#     search_fields = ('name',)
#     prepopulated_fields = {'slug': ('name',)}

class AnswerAdmin(admin.ModelAdmin):
    list_display = ( 'post', 'created', 'id')
    list_filter = ( 'created',)
    search_fields = ('name', 'text')

admin.site.register(Answer, AnswerAdmin)


admin.site.register(Questions,QuestionAdmin)
# admin.site.register(Category,CategoryAdmin)