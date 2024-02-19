from django.db import models
from django.contrib.auth.models import User


# Главная таблица
class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name="Назва")

    # метод для вывода в админке названия категории
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"


# второстепенная(дочерняя) таблица
class Post(models.Model):
    # атрибут в классе = колонка в таблице
    title = models.CharField(max_length=30, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Опис")
    published_date = models.DateTimeField(auto_created=True, verbose_name="Дата")   # добавляет дату и время после написания поста
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категорія")   # связь между таблицами
    image = models.URLField(default="http://placehold.it/900x300", verbose_name="Фото")     # добавление картинки в пост
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Автор")

    # метод для вывода в админке названия заголовка поста
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Пости"



