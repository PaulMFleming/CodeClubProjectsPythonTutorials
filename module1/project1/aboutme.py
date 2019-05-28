#!/bin/python3

print('Hello!')

print("My favorite animals are cats:")
# use three commas in brackets to enter text
# to print in the exact way you type it
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

# Get users age as variable born
born = input("What year were you born? ")
# Convert born to a number
born = int(born)
# Calculate age in year 2032
age = 2032 - born
print("In the year 2025 you\ 'll be", age, 'years old!')
