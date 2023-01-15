from _ast import operator
from functools import reduce

from django.contrib.admin.templatetags.admin_list import results
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, FormView, DeleteView, UpdateView, FormMixin
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
# Create your views here.
from django.contrib.auth import authenticate
from notifications.signals import notify
from taggit.views import TagListMixin

from user_profile.forms import CustomUserProfile
from .models import *
from taggit.models import Tag
from .utils import *
from django.db.models import Q, F
from django.http import Http404, HttpResponseRedirect
from .forms import *

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



class TagMixin(object):

    def get_context_data(self, **kwargs):
        context = super(TagMixin, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context


class MainListVIew(TagMixin, DataMixin, ListView):
    paginate_by = 7
    model = Questions  # выбирает все записи из таблицы и отображает их в виде списка
    template_name = 'blog/all_questions.html'
    context_object_name = 'posts'



    def get_context_data(self, *, object_list=None,
                         **kwargs):  # формирует динамический и статический контекст, который передается в шаблон
        context = super().get_context_data(**kwargs)  # получаем уже сформированый контекст ListView
        c_def = self.get_user_context(title='Главная страница - Mambr')
        # через self обращаемся ко всем методам базового класса DataMixin
        return {**context, **c_def}  # объядиняем словарь

    def get_queryset(self, *, object_list=None, **kwargs):
        q = self.request.GET.get("search", '')

        object_list = Questions.objects.filter(Q(q_name__icontains=q))
        return object_list.filter(is_published=True).order_by('-time_create')


class TagListView(TagMixin, ListView):
    paginate_by = 7
    model = Questions  # выбирает все записи из таблицы и отображает их в виде списка
    template_name = 'blog/all_questions.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Questions.objects.filter(tags__slug=self.kwargs.get('slug'))


class SuccessMessageMixin:
    @property
    def success_msg(self):
        return False

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super().form_valid(form)

    # def get_success_url(self):
    #     return reverse  (self.success_url, self.object.slug)
    def get_success_url(self):
        return '%s?id=%s' % (self.success_url, self.object.slug)



class MoreDetailsQuestion(SuccessMessageMixin, FormMixin, DetailView):
    model = Questions
    template_name = 'blog/more_q.html'
    pk_url_kwarg = 'q_pk'
    context_object_name = 'more_q'
    form_class = AnswerForm
    success_url = reverse_lazy('question')
    success_msg = 'Запись успешно обновлена'


    def get_success_url(self):
        return reverse_lazy('question', kwargs={'q_pk':self.get_object().id})

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['more_q']
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
                parent_obj = Answer.objects.get(id=form.parent_id)
                replay_comment = form.save(commit=False)
                replay_comment.parent = parent_obj
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.post = self.get_object()
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)



class QuestionDeleteView(LoginRequiredMixin, DeleteView):
    model = Questions
    context_object_name = 'delete_form'
    success_url = reverse_lazy('home')
    success_msg = 'Все ок'
    pk_url_kwarg = "q_pk"

    def post(self, request, *args, **kwargs):
        messages.success(self.request, self.success_msg)
        return super().post(request)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.request.user != self.object.author:
            return self.handle_no_permission()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

# class AnswerDeleteView(LoginRequiredMixin, DeleteView):
#     model = Answer
#     context_object_name = 'ans_delete_form'
#     success_url = reverse_lazy('home')
#     success_msg = 'Все ок'
#
#     def post(self, request, *args, **kwargs):
#         messages.success(self.request, self.success_msg)
#         return super().post(request)
#
#     def dispatch(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         if self.request.user != self.object.author:
#             return self.handle_no_permission()
#         success_url = self.get_success_url()
#         self.object.delete()
#         return HttpResponseRedirect(success_url)


class UpdateQuestionView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Questions
    template_name = 'blog/add_question.html'
    form_class = QuestionForm
    success_url = reverse_lazy('home')
    context_object_name = 'form'
    success_msg = 'Запись успешно обновлена'
    pk_url_kwarg = "q_pk"


    def get_success_url(self):
        return reverse_lazy('question', kwargs={'q_pk':self.get_object().id})
    def get_context_data(self, **kwargs):
        kwargs['update_button'] = True
        return super().get_context_data(**kwargs)

    def get_form_kwargs(self):
        """Return the keyword arguments for instantiating the form."""
        kwargs = super().get_form_kwargs()
        if self.request.user != kwargs['instance'].author:
            return self.handle_no_permission()
        return kwargs



class AddQuestion(SuccessMessageMixin, CreateView):
    model = Questions
    template_name = 'blog/add_question.html'
    form_class = QuestionForm
    success_msg = 'Запись успешно добавлена'
    success_url = reverse_lazy('home')
    context_object_name = 'form'

    def form_valid(self, form):
        self.object = form.save(commit=False)  # создаем экземпляр
        self.object.author = self.request.user  # получаем текущего user
        self.object.save()  # сохраняем в бд
        return super().form_valid(form)







