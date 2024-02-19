from django.shortcuts import render, get_object_or_404, redirect
from . models import Post, Category
from .forms import PostForm
import datetime
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator                # для переключения страничек
from django.contrib.auth import logout
# Create your views here.


# метод для формирования категорий для отображения справа на странице
def get_categories():
    all = Category.objects.all()
    count = all.count()
    half = count / 2 + count % 2
    first_half = all[:half]
    second_half = all[half:]
    return {'cat1': first_half, 'cat2': second_half}


def index(request):
    # posts = Post.objects.filter(title__contains="django")  # фильтрация данных (поиск)
    # posts = Post.objects.filter(published_date__year="2024")
    # posts = Post.objects.filter(category__name="news")
    # login = request.POST.get('login')
    # password = request.POST.get('password')
    #
    # if login == 'admin' and password == '123456':
    #     return render(request, 'blog/index.html', {'login': login}, )#{"posts": posts})
    #
    # elif login == 'user' and password == '123456':
    #     return render(request, 'blog/index.html', {'login': login})
    # else:
    #     return render(request, 'blog/errorEnter.html')

    posts = Post.objects.all()

    paginator = Paginator(posts, 2)                                 # отображение количества постов
    page_number = request.GET.get("page")                           # и переключение страничек
    page_obj = paginator.get_page(page_number)
    context = {'posts': page_obj}

    context.update(get_categories())
    return render(request, 'blog/index.html', context)


def post(request, id=None):
    posts = get_object_or_404(Post, pk=id)                          # перенаправление на выбранный пост
    context = {'posts': posts}
    context.update(get_categories())
    return render(request, 'blog/post.html', context)


#  отфильтровуем выбранные посты
def category(request, id=None):
    c = get_object_or_404(Category, pk=id)
    posts = Post.objects.filter(category=c).order_by("-published_date")
    context = {'posts': posts}
    context.update(get_categories())
    return render(request, 'blog/index.html', context)


# чтоб сделать поиск по нескольким условиям, нужно импортировать Q
from django.db.models import Q


def search(request):
    query = request.POST.get('query')
    posts = Post.objects.filter(Q(content__icontains=query) | Q(title__icontains=query))  # поиск по контенту | и по
    context = {'posts': posts}                                                            # заголовку
    context.update(get_categories())
    return render(request, 'blog/index.html', context)


@login_required   # декоратор для
# вьюшка для отображения создания нового поста
def create(request):
    if request.method == 'POST':
        form = PostForm(data=request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = datetime.datetime.now()
            post.user = request.user
            post.save()
            form.save_m2m()
        return redirect('index')
    form = PostForm()
    context = {'form': form}
    context.update(get_categories())
    return render(request, 'blog/create.html', context)


# def add_comment(request):
#     pass

# вьюшка для выхода
def logout_view(request):
    logout(request)
    return redirect('/')    # на главную страницу сайта
