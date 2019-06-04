#!/bin/python3

# import randint to generate random numbers
from random import randint

player = input('cat (c), dog (d) or ferret (f)?')

print(player, 'vs', end=' ')

chosen = randint(1, 3)

if chosen == 1:
    computer = 'c'

elif chosen == 2:
    computer = 'd'

else:
    computer = 's'

print(computer)

if player == computer:
    print('DRAW!')

elif player == 'c' and computer == 'd':
    print('Player Wins!')

elif player == 'd' and computer == 'c':
    print('Comuter wins!')

elif player == 'f' and computer == 'd':
    print('Player Wins!')

elif player == 'd' and computer == 'f':
    print('Computer Wins!')

elif player == 'c' and computer == 'f':
    print('Player Wins!')

elif player == 'f' and computer == 'c':
    print('Computer Wins!')


