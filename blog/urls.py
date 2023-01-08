from .views import *
from tgmsg.views import *
from user_profile.views import *
from django.urls import path

urlpatterns = [
    path('', MainListVIew.as_view(), name='home'),
    path('tag/<slug>/', TagListView.as_view(), name='taggit'),
    path('question/<int:q_pk>/', MoreDetailsQuestion.as_view(), name='question'),
    path('add_question/', AddQuestion.as_view(), name='add_q'),
    path('delete/<int:q_pk>/', QuestionDeleteView.as_view(), name='delete'),
    path('ans_delete/<int:q_pk>/', AnswerDeleteView.as_view(), name='ans_delete'),
    path('send_msg/<int:q_pk>/', send_tg,name='send_msg'),
    path('update/<int:q_pk>/', UpdateQuestionView.as_view(), name='edit')

]
