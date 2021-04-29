from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post
from random import choice


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


# TIC TAC TOE
# # GLOBALS
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9], 0
]

colors = [['-outline-dark', '-outline-dark', '-outline-dark', ] for _ in range(3)]


def tictactoe(request):
    resetGrid()
    data = {
      'title': 'Tic Tac Toe',
      'btn1': grid[0][0], 'btn2': grid[0][1], 'btn3': grid[0][2],
      'btn4': grid[1][0], 'btn5': grid[1][1], 'btn6': grid[1][2],
      'btn7': grid[2][0], 'btn8': grid[2][1], 'btn9': grid[2][2],
      'col1': colors[0][0], 'col2': colors[0][1], 'col3': colors[0][2],
      'col4': colors[1][0], 'col5': colors[1][1], 'col6': colors[1][2],
      'col7': colors[2][0], 'col8': colors[2][1], 'col9': colors[2][2]
    }
    return render(request, 'blog/tictactoe.html', data)


def resetGrid():
    global grid
    global colors
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9], 0
    ]
    colors = [['-warning', '-warning', '-warning', ] for _ in range(3)]


def checkbtn(request):
    global grid
    global colors
    answer = request.GET
    flag = 0
    print(colors)
    for key, value in answer.items():
        if value and value != 'O' and value != 'X':
            try:
                i = (int(value) - 1) // 3
                j = int(value) - 3 * i - 1
                grid[i][j] = 'X'
                colors[i][j] = '-secondary'
                grid[3] += 1
            except ValueError:
                pass
            flag = 1

    if flag:
        while True:
            if grid[3] == 5:  # max movements
                break
            i = choice([0, 1, 2])
            j = choice([0, 1, 2])
            if grid[i][j] != 'X' and grid[i][j] != 'O':
                grid[i][j] = 'O'
                colors[i][j] = '-info'
                break

    data = {
        'title': 'Tic Tac Toe',
        'btn1': grid[0][0], 'btn2': grid[0][1], 'btn3': grid[0][2],
        'btn4': grid[1][0], 'btn5': grid[1][1], 'btn6': grid[1][2],
        'btn7': grid[2][0], 'btn8': grid[2][1], 'btn9': grid[2][2],
        'col1': colors[0][0], 'col2': colors[0][1], 'col3': colors[0][2],
        'col4': colors[1][0], 'col5': colors[1][1], 'col6': colors[1][2],
        'col7': colors[2][0], 'col8': colors[2][1], 'col9': colors[2][2]
            }

    return render(request, 'blog/tictactoe.html', data)


