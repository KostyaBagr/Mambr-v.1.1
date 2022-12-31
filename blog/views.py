from _ast import operator
from functools import reduce

from django.contrib.admin.templatetags.admin_list import results
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, FormView, DeleteView, UpdateView, FormMixin
from django.http import HttpResponse, JsonResponse
# Create your views here.
from .models import *
from .utils import *
from django.db.models import Q
from django.http import Http404, HttpResponseRedirect
from .forms import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class MainListVIew(DataMixin, ListView):
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

    def get_queryset(self):
        q = self.request.GET.get("search", '')
        object_list = Questions.objects.filter(Q(q_name__icontains=q))

        return object_list

    # def get_queryset(self):
    #     return Questions.objects.filter(is_published=True)  # возвращвем только опубликованные записиаписи


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
        return '%s?slug=%s' % (self.success_url, self.object.slug)


class ShowCategoryView(ListView):
    paginate_by = 7
    model = Questions  # выбирает все записи из таблицы и отображает их в виде списка
    template_name = 'blog/all_questions.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Questions.objects.filter(q_cat__slug=self.kwargs['cat_slug'])

    def get_context_data(self, *, object_list=None,
                         **kwargs):  # формирует динамический и статический контекст, который передается в шаблон
        context = super().get_context_data(**kwargs)  # получаем уже сформированый контекст ListView
        context['title'] = 'Категория - ' + str(context['posts'][0].q_cat)
        context['cat_selected'] = context['posts'][0].q_cat_id
        return context


class MoreDetailsQuestion(SuccessMessageMixin, FormMixin, DetailView):
    model = Questions
    template_name = 'blog/more_q.html'
    slug_url_kwarg = 'q_slug'
    context_object_name = 'more_q'
    form_class = AnswerForm
    success_url= reverse_lazy('question')
    success_msg = 'Запись успешно обновлена'

    def get_success_url(self, **kwargs):
        return reverse_lazy('question', kwargs={'q_slug': self.get_object().slug})

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['more_q']
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            # print(self.get_object())
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.post = self.get_object()
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)



# class DeleteQuestionView(DeleteView):
#     model = Questions
#     context_object_name = 'more_q'
#     template_name = 'blog/more_q.html'
#     success_url = reverse_lazy('home')
#     success_msg = 'Запись удалена'
#
#     def post(self, request, *args, **kwargs):
#         messages.success(self.request, self.success_msg)
#         return super().post(request)
@login_required
def delete_q(request, slug):
    post_to_delete = Questions.objects.get(slug=slug)
    post_to_delete.delete()
    # print(request.user)
    return HttpResponse('Запись успешно удалена')



class UpdateQuestionView(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    model = Questions
    template_name = 'blog/add_question.html'
    form_class = QuestionForm
    success_url = reverse_lazy('home')
    context_object_name = 'form'
    success_msg = 'Запись успешно обновлена'

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
        self.object = form.save(commit=False)#создаем экземпляр
        self.object.author = self.request.user# получаем текущего user
        self.object.save()# сохраняем в бд
        return super().form_valid(form)



