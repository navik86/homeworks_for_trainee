import random
import tkinter.messagebox
from tkinter import *

board_size = 10
number_for_win = 5
board = [[0] * board_size for item in range(board_size)]

game_run = True
field = []
cross_count = 0

root = Tk()
root.title('tic-tac-toe')
root.geometry("780x614")
root.resizable(False, False)


def render_board_game():
    for row in range(board_size):
        line = []
        for col in range(board_size):
            button = Button(root, text=' ', width=4, height=2,
                            font=('Verdana', 14, 'bold'),
                            background='#555',
                            command=lambda row=row, col=col: click(row, col))
            button.grid(row=row, column=col, sticky='nsew')
            line.append(button)
        field.append(line)
    btn = Button(root, text='New game', command=new_game, font=('Courier', 14, 'bold'), background='#555')
    btn.grid(row=board_size + 1, column=0, columnspan=board_size, sticky='nsew')


def new_game():
    global game_run, cross_count, board
    for row in range(10):
        for col in range(10):
            field[row][col]['text'] = ' '
            field[row][col]['background'] = 'lavender'
    game_run = True
    cross_count = 0
    board = [[0] * board_size for item in range(board_size)]


def click(row, col):
    global game_run, cross_count
    if game_run and field[row][col]['text'] == ' ':
        field[row][col]['text'] = 'X'
        board[row][col] = -1
        cross_count += 1
        win = wins(board, -1)
        if win:
            tkinter.messagebox.showinfo("Info", "You lose!")
            game_run = False

        if game_run and cross_count < 50:
            computer_step()
            win = wins(board, 1)
            if win:
                tkinter.messagebox.showinfo("Info", "You win!")
                game_run = False


def check_line(a1, a2, a3, smb):
    global game_run
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == smb:
        a1['background'] = a2['background'] = a3['background'] = 'pink'
        game_run = False


def wins(state, player):
    def win_list(num_list, number_for_win):

        return [
            num_list[num: num + number_for_win] for num in range(len(num_list) - 4)
        ]

    horizontally = []
    vertically = []
    diagonally_1 = []
    diagonally_2 = []
    count = 0
    count_2 = board_size - 1

    for w in range(board_size):
        tmp1 = []
        tmp2 = []
        for z in range(board_size):
            tmp1.append(state[w][z])
            tmp2.append(state[z][w])
        horizontally += win_list(tmp1, number_for_win)
        vertically += win_list(tmp2, number_for_win)
        diagonally_1.append(tmp1[count])
        diagonally_2.append(tmp2[count_2])
        count += 1
        count_2 -= 1

    diagonally_1 = win_list(diagonally_1, number_for_win)
    diagonally_2 = win_list(diagonally_2, number_for_win)

    win_state = [*horizontally, *vertically, *diagonally_1, *diagonally_2]

    if [player] * number_for_win in win_state:
        return True
    else:
        return False


def computer_step():
    while True:
        row = random.randint(0, 9)
        col = random.randint(0, 9)
        if field[row][col]['text'] == ' ':
            field[row][col]['text'] = 'O'
            board[row][col] = 1
            break


render_board_game()
root.mainloop()