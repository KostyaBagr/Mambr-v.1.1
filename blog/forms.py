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



class QuestionForm(forms.ModelForm):
    class Meta:
        model = Questions
        fields = ['q_name', 'tags', 'q_text']

        widgets = {
            'q_name': forms.TextInput(attrs={'class': 'form-name'}),
            'slug': forms.TextInput(attrs={'class': 'form-slug'}),

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['q_text'].widget.attrs.update({'id': 'text_test'})


        # self.fields['q_cat'].widget.attrs.update(size='40')

# вопрос
# vopros
