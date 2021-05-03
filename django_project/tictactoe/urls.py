from django.urls import path
from . import views


urlpatterns = [
    path('tic-tac-toe/', views.tictactoe, name='tictactoe'),
    path('tic-tac-toe/check/', views.checkbtn, name="tictactoe-check"),
    path('tic-tac-toe/success/', views.tictactoesuccess, name='tictactoe-success'),
    path('tic-tac-toe/failure/', views.tictactoefailure, name='tictactoe-failure'),
    path('tic-tac-toe/draw/', views.tictactoedraw, name='tictactoe-draw')
]