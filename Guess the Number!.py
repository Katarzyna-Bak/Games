# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

#import necessary modules
import simplegui
import random
import math

# initialize global variables used in your code
search_range = 100
remaining_chances = 7
secret_number = random.randrange(100)

# helper function to start and restart the game
def new_game():
    global search_range
    
    if (search_range==100):
        range100()
    elif (search_range==1000):
        range1000()
    
# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game  
    global search_range
    global secret_number
    global remaining_chances
    
    search_range = 100
    secret_number = random.randrange(100)
    remaining_chances = 7
    
    print('\nNew game started!\n\nThe range is set to 0-{}.\nYou have {} guesses.'.format(search_range, remaining_chances))
    return search_range, secret_number, remaining_chances

def range1000():
    # button that changes the range to [0,1000) and starts a new game 
    global search_range
    global secret_number
    global remaining_chances
    
    search_range = 1000
    secret_number = random.randrange(1000)
    remaining_chances = 10
    
    print('\nNew game started!\n\nThe range is set to 0-{}.\nYou have {} guesses.'.format(search_range, remaining_chances))
    return search_range, secret_number, remaining_chances

    
def input_guess(guess):
    # main game logic goes here
    global remaining_chances
    
    if remaining_chances >= 0:
        guess = int(guess)
        print('\nGuess was {}'.format(guess))
    
        if guess != secret_number:
            if guess > secret_number:
                print('Lower')
                remaining_chances -= 1
            else:
                print('Higher')
                remaining_chances -= 1
            
            if remaining_chances != 0:
                print('The number of remaining guesses: {}'.format(remaining_chances))
            else:
                print('You lose. The correct number was {}'.format(secret_number))
                print('Good luck next time!')
                new_game()
        else:
            print('Correct')
            print('You win!')
            new_game()
    
# create frame
frame = simplegui.create_frame('Guess the number', 200, 200)

# register event handlers for control elements and start frame
frame.add_button('Range is [0, 100)', range100, 200)
frame.add_button('Range is [0, 1000)', range1000, 200)
frame.add_button('Start a new game', new_game, 200)
frame.add_input('Enter your guess', input_guess, 200)

# call new_game 
new_game()
frame.start()

# always remember to check your completed program against the grading rubric