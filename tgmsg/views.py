from django.shortcuts import render
from blog.models import Questions
from django.http import HttpResponse
from tgmsg.tgBot import *
import requests
# Create your views here
from django.shortcuts import get_object_or_404
from django.views.generic import ListView

# class Send(ListView):
#     template_name = 'blog/more_q.html'
#     context_object_name = 'telegram_form'


def send_tg(request,q_pk):
        if request.method == "POST":
                get_path = request.path_info[10:]
                link = 'http://127.0.0.1:8000/question/'+ get_path
                # print(link)
                question_name = get_object_or_404(Questions, pk=q_pk)
                sendTg(question_name,link)
                dict = {
                        'question_name' : question_name
                }
                return render(request, 'blog/okey_msg.html', dict)

