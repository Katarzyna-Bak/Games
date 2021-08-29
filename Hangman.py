"""
Project #2: Hangman
"""

import os
from time import sleep
import random

gallows = [
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '_', '_', '_', '_', '_', ' ', ' '],
[' ', 'U', 's', 'e', 'd', ' ', 'l', 'e', 't', 't','e', 'r', 's', ':', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '-', '-', '-', '-', '-'],
[' ', 'Y', 'o', 'u', 'r', ' ', 'w', 'o', 'r', 'd',':', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

#draw the playing board
def drawGallows(gallows):
    for row in range(len(gallows)):
        for column in range(34):
            if column != 33:
                print(gallows[row][column], end='')
            else:
                print(gallows[row][column])

#clear the screen when function is called
def clearScreen():
    _ = os.system('cls')

def generateWord(file):
    with open(file) as f:
        fileContent = f.read()
    lines = fileContent.splitlines()
    line_number = random.randrange(0, len(lines))
    return lines[line_number]

#variables
repeatGame = True
mistakes = 0
count = 0

#game
while repeatGame == True:
    #allow the user to select between game modes
    print('\nWelcome to the hangman game.')
    print('Which mode do you want to play?\n1 - 1-player mode\n2 - 2-player mode.')

    #check if the user selected one of the available options
    validAnswer = False
    while validAnswer == False:
        selection = input('\nType 1 or 2 to proceed: ')
        try:
            selection = int(selection)
            if selection == 1 or selection == 2:
                validAnswer = True
            else:
                print('Invalid input, try again.')
        except:
            print('Invalid input, try again.')

    if selection == 1:
        word = generateWord('Hangman_list_of_words.txt')
        print('\nWord selected, you can start playing')
    else:
        print('\nPlayer 1 turn:')
        print("\nPlease type in the word for player 2 to guess.\nThe word should be longer than 5 and shorter than 23 letters.")

        #check if the word is acceptable
        validWord = False
        while validWord == False:
            word = input('\nThe word is: ')
            if word.isalpha() == True:
                #check the word's length
                if len(word) < 5:
                    print('The word is too short.')
                elif len(word) > 23:
                    print('The word is too long.')
                else:
                    validWord = True
            else:
                print('Invalid word. The word cannot contain numbers.')  
        sleep(2)
        clearScreen()
        print('Player 2 turn:') 
    word = word.upper()

    #clear shell
    
    #draw the word lines
    column = 1
    for i in range(len(word)):
        gallows[8][column] = '_ '
        column += 1

    #variables and list used in the embedded loop
    win = False
    lose = False
    usedLetters = []

    #check if the player used a valid letter which was not used before
    while win == False and lose == False:
        drawGallows(gallows)
        validLetter = False
        while validLetter == False:
            playerInput = input('\nWhich letter do you want to check? ')
            playerInput = playerInput.upper()
            if playerInput.isalpha() == True:
                if len(playerInput) > 1:
                    print('You can only check 1 letter at a time')
                elif playerInput not in usedLetters:
                    validLetter = True
                else:
                    print('Letter already used')
            else:
                print('Invalid input, please use one of the available letters.')

        #add the selected letter to the usedLetters list
        usedLetters.extend(playerInput)

        column = 1
        row = 2
        #print the used letters on the board
        rangeL = len(usedLetters)
        for letter in range(rangeL):
            if column <= 17 and gallows[row][column] == ' ':
                gallows[row][column] = usedLetters[letter]
            elif column <= 17 and gallows[row][column] != ' ':
                gallows[row][column] = usedLetters[letter]
            else:
                row += 1
                column = 1
                gallows[row][column] = usedLetters[letter]
            column += 2
            
        #check if the letter appears in the selected word
        index = []
        for ind in range(len(word)):
            if playerInput == word[ind]:
                index.append(ind+1)
                count += 1 #count correctly assigned letters - needed for the win criteria

        if index != []:
            for ind in index:
                gallows[8][ind] = playerInput

        #set win to True if count 
        if count == len(word):
            win = True

        #increase mistake numer if the word doesn't have the selected letter
        if playerInput not in word:
            mistakes += 1
                
        #draw a part of the hangman when a misake is recorded
        if mistakes == 1:
            gallows[2][-7] = 'O'
        elif mistakes == 2:
            gallows[3][-7] = '|'
        elif mistakes == 3:
            gallows[3][-8] = '/'
        elif mistakes == 4:
            gallows[3][-6] = '\\'
        elif mistakes == 5:
            gallows[4][-7] = '|'
        elif mistakes == 6:
            gallows[5][-8] = '/'
        #set lose to True when 7 mistakes are recorded
        elif mistakes == 7:
            gallows[5][-6] = '\\'
            drawGallows(gallows)
            lose = True

        #print the required messages
        if win == True:
            print('\nCongratulations, you won!')
        elif lose == True:
            print('\nYou lost.')
            print('The word you were looking for is: {}'.format(word))
            
    #allow the player to play again without restarting the program
    repeat = input('\nDo you want to play again? [Y/N] ')
    if repeat == 'y' or repeat == 'Y':
        repeatGame = True
    else:
        repeatGame = False