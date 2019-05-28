#!/bin/python3

# import randint to generate random numbers
from random import randint

# Get input for players choice
player = input('rock (r), paper (p) or scissors(s)?')

# Turn players choice into ascii art
if player == 'r':
    player_icon = '0'

elif player == 'p':
    player_icon ='_'

else:
    player_icon ='>8'

# Print Player Choice VS Computer Choice in ASCII
print(player_icon, 'vs', end=' ')

# Computer chooses at random
chosen = randint(1, 3)

# Convert computer choice into ASCII
if chosen == 1:
    computer = 'r'
    print('0')

elif chosen == 2:
    computer = 'p'
    print('_')

else:
    computer == 's'
    print('>8')

# Calculate Winner
if player == computer:
    print('DRAW!')

elif player == 'r' and computer == 's':
    print('Player Wins!')

elif player == 'r' and computer == 'p':
    print('Comuter wins!')

elif player == 'p' and computer == 'r':
    print('Player Wins!')

elif player == 'p' and computer == 's':
    print('Computer Wins!')

elif player == 's' and computer == 'p':
    print('Player Wins!')

elif player == 's' and computer == 'r':
    print('Computer Wins!')


