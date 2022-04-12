#170 project 1
import math




# Create default puzzle

# Welcome message
print("Welcome to 862073206 8 puzzle solver.")

# Create puzzle
pmode = eval(input("Type \"1\" to use a default puzzle, or \"2\" to enter your own puzzle."))
while pmode != 1 and pmode != 2:
    pmode = eval(input("Error: invalid input, please try again"))

# Default puzzle
if pmode == '1':
    temp = 0
# Custom puzzle
elif pmode == '2':
    print("Enter your puzzle, use a zero to represent the blank")
    print("Enter the frist row, use space or tabs between numbers", end='')
    print("Enter the second row, use space or tabs between numbers", end='')
    print("Enter the third row, use space or tabs between numbers", end='')

# Select algorithm
print("Enter your choice of algorithm")
print("1: Uniform Cost Search")
print("2: A* with the Misplaced Tile heuristic")
print("3: A* with the Eucledian Distance heuristic")
amode = eval(input())