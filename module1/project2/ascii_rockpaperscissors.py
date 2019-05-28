#!/bin/python3

# import randint to generate random numbers
from random import randint

player = input('rock (r), paper (p) or scissors(s)?')

print(player, 'vs', end=' ')

chosen = randint(1, 3)

if chosen == 1:
    computer = 'r'
    print('0')

elif chosen == 2:
    computer = 'p'
    print('_')

else:
    computer = 's'
    print('>8')

print(computer)

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


