from django.shortcuts import render, redirect
from random import choice

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
    return render(request, 'tictactoe/tictactoe.html', data)


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
    game_active = True

    if game_active:
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
                if checkwin()[0] and checkwin()[1] == 'User':
                    return redirect('tictactoe-success')
                    game_active = False
                    flag = 0

        if flag:
            while True:
                if grid[3] == 5:  # max movements
                    break
                i = choice([0, 1, 2])
                j = choice([0, 1, 2])
                if grid[i][j] != 'X' and grid[i][j] != 'O':
                    grid[i][j] = 'O'
                    colors[i][j] = '-info'
                    if checkwin()[0] and checkwin()[1] == 'AI':
                        return redirect('tictactoe-failure')
                        game_active = False
                    break

        if grid[3] == 5 and not checkwin()[0]:
            return redirect('tictactoe-draw')

    data = {
        'title': 'Tic Tac Toe',
        'btn1': grid[0][0], 'btn2': grid[0][1], 'btn3': grid[0][2],
        'btn4': grid[1][0], 'btn5': grid[1][1], 'btn6': grid[1][2],
        'btn7': grid[2][0], 'btn8': grid[2][1], 'btn9': grid[2][2],
        'col1': colors[0][0], 'col2': colors[0][1], 'col3': colors[0][2],
        'col4': colors[1][0], 'col5': colors[1][1], 'col6': colors[1][2],
        'col7': colors[2][0], 'col8': colors[2][1], 'col9': colors[2][2]
            }

    return render(request, 'tictactoe/tictactoe.html', data)


def checkwin():
    global grid
    user_win = ['X', 'X', 'X']
    ai_win = ['O', 'O', 'O']

    for row in grid:
        if row == user_win:
            return True, 'User'
        elif row == ai_win:
            return True, "AI"

    for i in range(len(grid)-1):
        stack = [grid[0][i], grid[1][i], grid[2][i]]
        if stack == user_win:
            return True, 'User'
        elif stack == ai_win:
            return True, "AI"

    stack = [grid[0][0], grid[1][1], grid[2][2]]
    if stack == user_win:
        return True, 'User'
    elif stack == ai_win:
        return True, "AI"

    stack = [grid[0][2], grid[1][1], grid[2][0]]
    if stack == user_win:
        return True, 'User'
    elif stack == ai_win:
        return True, "AI"
    return False, 'Draw'


def tictactoesuccess(request):
    data = {
        'title': 'Tic Tac Toe',
        'btn1': grid[0][0], 'btn2': grid[0][1], 'btn3': grid[0][2],
        'btn4': grid[1][0], 'btn5': grid[1][1], 'btn6': grid[1][2],
        'btn7': grid[2][0], 'btn8': grid[2][1], 'btn9': grid[2][2],
        'col1': colors[0][0], 'col2': colors[0][1], 'col3': colors[0][2],
        'col4': colors[1][0], 'col5': colors[1][1], 'col6': colors[1][2],
        'col7': colors[2][0], 'col8': colors[2][1], 'col9': colors[2][2]
    }

    return render(request, 'tictactoe/tictactoe_success.html', data)


def tictactoefailure(request):
    data = {
        'title': 'Tic Tac Toe',
        'btn1': grid[0][0], 'btn2': grid[0][1], 'btn3': grid[0][2],
        'btn4': grid[1][0], 'btn5': grid[1][1], 'btn6': grid[1][2],
        'btn7': grid[2][0], 'btn8': grid[2][1], 'btn9': grid[2][2],
        'col1': colors[0][0], 'col2': colors[0][1], 'col3': colors[0][2],
        'col4': colors[1][0], 'col5': colors[1][1], 'col6': colors[1][2],
        'col7': colors[2][0], 'col8': colors[2][1], 'col9': colors[2][2]
    }
    return render(request, 'tictactoe/tictactoe_failure.html', data)


def tictactoedraw(request):
    data = {
        'title': 'Tic Tac Toe',
        'btn1': grid[0][0], 'btn2': grid[0][1], 'btn3': grid[0][2],
        'btn4': grid[1][0], 'btn5': grid[1][1], 'btn6': grid[1][2],
        'btn7': grid[2][0], 'btn8': grid[2][1], 'btn9': grid[2][2],
        'col1': colors[0][0], 'col2': colors[0][1], 'col3': colors[0][2],
        'col4': colors[1][0], 'col5': colors[1][1], 'col6': colors[1][2],
        'col7': colors[2][0], 'col8': colors[2][1], 'col9': colors[2][2]
    }
    return render(request, 'tictactoe/tictactoe_draw.html', data)
