from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView             # аутентификация авторизация пользователя


urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.index, name='blog'),
    path('blog/post/<int:id>/', views.post, name='post'),
    path('blog/category/<int:id>/', views.category, name='category'),   # urls для категорий
    path('blog/search/', views.search, name='search'),                  # url для поиска
    path('blog/create/', views.create, name='create'),                  # маршрут для перехода на страницу создания нового поста
    path('login/', LoginView.as_view(), name='blog_login'),             # вьюшка для аутентификации
    # path('logout/', LogoutView.as_view(), name='blog_logout')           # вьюшка для выхода
    path('accounts/logout/', views.logout_view, name='blog_logout'),

]
