from django.core.cache import cache
from .models import *

class DataMixin:
    def get_user_context(self, **kwargs):  # метод создает контекст для шаблона
        context = kwargs  # формируем словарь из параметров переданных ф-ией get_user_context
        context['cat_selected'] = 0
        return context

        # cats = cache.get('cats') # береим из данные из кеша if True
        # if not cats: # if False
        #     cats = Category.objects.annotate(Count('women'))  #
        #     cache.set('cats', cats,60) # заносим двнные в кеш
