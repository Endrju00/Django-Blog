from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
    path('tic-tac-toe/', views.tictactoe, name='blog-tictactoe'),
    path('tic-tac-toe/check/', views.checkbtn, name="check"),
    path('tic-tac-toe/success/', views.tictactoesuccess, name='tictactoe-success'),
    path('tic-tac-toe/failure/', views.tictactoefailure, name='tictactoe-failure'),
    path('tic-tac-toe/draw/', views.tictactoedraw, name='tictactoe-draw')
]