# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions
import random

def name_to_number(name):
    # delete the following pass statement and fill in your code below
    valid_values = {'rock': 0, 'Spock': 1, 'paper': 2, 'lizard': 3, 'scissors': 4}
    
    if name in valid_values.keys():
        return valid_values[name]
    else:
        return 'Please provide a valid input - rock, Spock, paper, lizard or scissors'

    # convert name to number using if/elif/else
    # don't forget to return the result!

def number_to_name(number):
    # delete the following pass statement and fill in your code below
    valid_numbers = {0: 'rock', 1: 'Spock', 2: 'paper', 3: 'lizard', 4: 'scissors'}
    
    if number in valid_numbers.keys():
        return valid_numbers[number]
    else:
        return 'Please provide a valid number between 0 and 4.'
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    

def rpsls(player_choice): 
    # delete the following pass statement and fill in your code below  
    # print a blank line to separate consecutive games
    print('\n')
    
    # print out the message for the player's choice
    print('Player chooses {}'.format(player_choice))
    
    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)

    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0, 5)
    
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    
    # print out the message for computer's choice
    print('Computer chooses {}'.format(comp_choice))
    
    # compute difference of comp_number and player_number modulo five
    result = (comp_number - player_number) % 5
    
    # use if/elif/else to determine winner, print winner message
    if result == 1 or result == 2:
        print('Computer wins!')
    elif result == 0:
        print("It's a draw!")
    else:
        print('Player wins!')
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric