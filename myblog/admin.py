from django.contrib import admin
from . models import Post, Category

# регистрация созданных моделей Post и Category в models.py

admin.site.register(Post)
admin.site.register(Category)
