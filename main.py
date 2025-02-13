# game designed to start as X and switch upon victory or draw
# can change with global variable and new_game func

import customtkinter
from tkinter import messagebox

# setup window
root = customtkinter.CTk()
root.title('TIC-TAC-TOE')
root.iconbitmap('images/file185.ico')
root.configure(bg='black')

# font stylings used in buttons
game_font = customtkinter.CTkFont(family='Helvetica', size=60, weight='bold')

# configure whether player X or O is active
def take_turn(row, col):
    global active_player

    if game[row][col] == '':
        game[row][col] = active_player
        board_buttons[row][col].configure(text=active_player)
        is_winner()
        active_player = 'O' if active_player == 'X' else 'X'

# identify winner or draw
def is_winner():
    combos = (game[0], game[1], game[2],
              [game[i][0] for i in range(3)],
              [game[i][1] for i in range(3)],
              [game[i][i] for i in range(3)],
              [game[i][2 - 1] for i in range(3)])
    # if any combination is satisfied then victor is declared
    for combo in combos:
        if combo[0] == combo[1] == combo[2] != '':
            declare_victory(combo[0])
    # if board is filled with no winning combination then game is a draw
    if all(game[i][j] != '' for i in range(3) for j in range(3)):
        declare_victory('TIE')

# decide a victor and display in messagebox
def declare_victory(player):
    if player == 'TIE':
        message = "IT'S A DRAW!"
    else:
        message = f'{player} WINS THE GAME!'
    messagebox.showinfo('Game Over', message)
    new_game()

# clear and reset game after messagebox is closed
def new_game():    
    global game
    game = [['', '', ''] for _ in range(3)]    
    for row in board_buttons:
        for button in row:
            button.configure(text='')

# create game board as buttons
# create a 3x3 grid using buttons
board_buttons = []
for i in range(3):
    row = []
    for j in range(3):        
        button = customtkinter.CTkButton(root, text='', text_color='white', fg_color='#8b5a2b', hover_color='#cd8500',
                                         font=game_font, width=100, height=100, command=lambda i=i, j=j: take_turn(i,j))
        button.grid(row=i, column=j, padx=10, pady=10)
        row.append(button)
    board_buttons.append(row)

# empty text from buttons and set X as the active marker
game = [['', '', ''] for _ in range(3)]
active_player = 'X'

# run main loop
root.mainloop()