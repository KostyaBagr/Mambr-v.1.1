from .views import *
from user_profile.views import *
from django.urls import path

urlpatterns = [
    path('', MainListVIew.as_view(), name='home'),
    path('question/<slug:q_slug>/', MoreDetailsQuestion.as_view(), name='question'),
    path('add_question/', AddQuestion.as_view(), name='add_q'),
    path('delete/<slug:slug>/', delete_q, name='delete'),
    path('category/<slug:cat_slug>/', ShowCategoryView.as_view(), name='category'),
    path('update/<slug:slug>/', UpdateQuestionView.as_view(), name='edit')

]
