# -*- coding: ANSI -*-

"""
Project #1: A Simple Game => Connect 4:

Rules:
- 2 players
- 2 coloured circles (red and black usually)
- enough pieces to fill the whole board
- to win, get 4 pieces in a horizontal, diagonal or vertical row
- board size: 6 vertical and 7 horizontal spaces
- pieces slide to bottom (bottom row is completed first)

ANSI code usage:
print('\033[1;32;40m Bright Green  \n')
    \033[  Escape code, this is always the same
    1 = Style, 1 for normal.
    32 = Text colour, 32 for bright green.
    40m = Background colour, 40 is for black.

    '\033[m' <- reset the shell colour after using ANSI codes

Issues spotted:
Problem spotted - the grid changes layout from time to time... How to deal with this?
Update the game once I learn how to manage this...
"""
#create coloured pieces for each player
#green - player 1
piecePlayer1= ' \033[1;32;40m{}'.format(u'\u2B24')+' \033[m'
#cyan - player 2
piecePlayer2 = ' \033[1;36;40m{}'.format(u'\u2B24')+' \033[m'

#define list storing all answers
currentField = [['   ', '   ', '   ', '   ', '   ', '   '], ['   ', '   ', '   ', '   ', '   ', '   '], ['   ', '   ', '   ', '   ', '   ', '   '], ['   ', '   ', '   ', '   ', '   ', '   '], ['   ', '   ', '   ', '   ', '   ', '   '], ['   ', '   ', '   ', '   ', '   ', '   '], ['   ', '   ', '   ', '   ', '   ', '   ']]
# print(currentField)

row = 5
player = 1
win = False

#draw the board
def drawBoard(field):
    for row in range(11):
        if row % 2 == 0:
            correctedRow = int(row / 2)
            for column in range(1, 14):
                if column % 2 == 1:
                    correctedColumn = int(column / 2)
                    if column != 13:
                        print(field[correctedColumn][correctedRow], end='')
                    else:
                        print(field[correctedColumn][correctedRow])
                else:
                    print('|', end = '')
        else:
            print('-' * 27)

#move the piece up if the cell is not "Empty"
def decreaseRow(field, column):
    row = 5
    while row >= 0:
        if field[column][row] == '   ':
            break
        else:
            row -= 1
    return row

# 4 in a row
def checkRows(field, piece):
    global win
    row = 0

    while row <= 5:
        for column in range(4):
            if (field[column][row] == piece) and (field[column+1][row] == piece) and (field[column+2][row] == piece) and (field[column+3][row] == piece):
                win = True
                break
        row += 1
    return win

# 4 in a column
def checkColumns(field, piece):
    global win
    column = 0

    while column <= 6:
        for row in range(3):
            if (field[column][row] == piece) and (field[column][row+1] == piece) and (field[column][row+2] == piece) and (field[column][row+3] == piece):
                win = True
                break
        column += 1
    return win

#4 diagonal
def checkDiagonal1(field, piece):
    global win

    row = 0
    while row <= 2:
        for column in range(4):
            if (field[column][row] == piece) and (field[column+1][row+1] == piece) and (field[column+2][row+2] == piece) and (field[column+3][row+3] == piece):
                win = True
                break
        row += 1

    row = 3
    while row >= 3 and row <= 5:
        for column in range(4):
            if (field[column][row] == piece) and (field[column+1][row-1] == piece) and (field[column+2][row-2] == piece) and (field[column+3][row-3] == piece):
                win = True
                break
        row += 1
    return win

#display win or draw messages depending on results
def winNotification(field, player):
    global win
    if win == True:
        print('Player {} wins!'.format(player))
    else:
        if field[0][0] != '   ' and field[1][0] != '   ' and field[2][0] != '   ' and field[3][0] != '   ' and field[4][0] != '   ' and field[5][0] != '   ' and field[6][0] != '   ':
            win = 'draw'
            print("Board full - It's a draw!")

#game
while win == False or win == 'draw':

    print('Player {} turn!'.format(player))
    column = int(input('Please specify to which column you want to add your game piece: ')) - 1

    if player == 1:
        row = decreaseRow(currentField, column)
        currentField[column][row] = piecePlayer1
        drawBoard(currentField)
        checkRows(currentField, piecePlayer1)
        checkColumns(currentField, piecePlayer1)
        checkDiagonal1(currentField, piecePlayer1)
        winNotification(currentField, player)

        player = 2

    else:
        row = decreaseRow(currentField, column)
        currentField[column][row] = piecePlayer2
        drawBoard(currentField)
        checkRows(currentField, piecePlayer2)
        checkColumns(currentField, piecePlayer2)
        checkDiagonal1(currentField, piecePlayer2)
        winNotification(currentField, player)

        player = 1