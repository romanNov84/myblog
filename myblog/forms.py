# ВОЗМОЖНОСТЬ ПОЛЬЗОВАТЕЛЮ СОЗДАВАТЬ СВОИ ПОСТЫ
from django import forms
from .models import Post


class PostForm(forms.ModelForm):               # форма для поста
    class Meta:                                # класс Мета дополнительно настроит пост форму
        model = Post                           # в основе формы будет лежать моделька Post
        exclude = ('published_date', 'user')   # exclude исключить поле с названием 'published_date',
                                               # при создании поста исключаем поле user

