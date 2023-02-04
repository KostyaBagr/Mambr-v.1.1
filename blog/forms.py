from django.core.exceptions import ValidationError

from .models import *
from django import forms
from django.forms import ModelForm, widgets


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['text']
        labels = {'text': 'Ваш ответ'}
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'id': 'test'})
    def send_email(self):
        send_answer_by_email.delay(
        self.cleaned_data['text'])



class QuestionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['difficult'].empty_label ='Сложность не выбрана'
    class Meta:
        model = Questions
        fields = {'q_name', 'tags', 'q_text', 'difficult'}
        labels ={
            'q_name': 'Суть вопроса',
            'tags':'Теги вопроса',
            'q_text': 'Детали вопроса',
            'difficult':'Сложность вопроса'
        }
        widgets = {
            'q_name': forms.TextInput(attrs={'class': 'form-name'}),
        }
    def clean_q_name(self):
        q_name = self.cleaned_data['q_name']
        if '?' not in q_name[-1]:
            raise ValidationError('Сформулируйте вопрос так, что бы в конце был "?"')
        if q_name[0].islower():
            raise ValidationError('Вопрос должен начинаться с заглавной буквы')
        if len(q_name) >200 or len(q_name) <15:
            raise ValidationError('Вопрос не может быть короче 15 и больше 200 символов')
        return q_name






# вопрос
# vopros
