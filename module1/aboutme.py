#!/bin/python3

print('Hello!')

print("My favorite animals are cats:")
print('''
    |\---/|
    | o_o |
     \_^_/
''')

print("I live in:")
print('''
 ___    __ __  ____   _      ____  ____  
|   \  |  |  ||    \ | |    |    ||    \ 
|    \ |  |  ||  o  )| |     |  | |  _  |
|  D  ||  |  ||     || |___  |  | |  |  |
|     ||  :  ||  O  ||     | |  | |  |  |
|     ||     ||     ||     | |  | |  |  |
|_____| \__,_||_____||_____||____||__|__|
''')

born = input("What year were you born? ")
born = int(born)
age = 2032 - born
print('In the year 2025 you\'ll be', age, 'years old!')
