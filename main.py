#170 project 1
import ast
import puzzle as p
import search as s


# Create default puzzle
if __name__ == "__main__":
    # Welcome message
    print("Welcome to 862073206 8 puzzle solver.")

    # Ask user how to build puzzle
    pmode = ast.literal_eval(input("Type \"1\" to use a default puzzle, or \"2\" to enter your own puzzle."))
    
    # Instantitate a puzzle object
    problem = p.Puzzle()

    # Default puzzle
    if pmode == '1':
        problem.build_default_table()
    # Custom puzzle
    elif pmode == '2':
        print("Enter your puzzle, use a zero to represent the blank")

        # Ask user for first row
        print("Enter the frist row, use space or tabs between numbers", end='')
        
        # Build first row
        input1, input2, input3 = int(ast.literal_eval(input.split()))
        problem.build_custom_table(0, 0, input1)
        problem.build_custom_table(0, 1, input2)
        problem.build_custom_table(0, 2, input3)

        # Ask user for second row
        print("Enter the second row, use space or tabs between numbers", end='')

        # Build second row
        input4, input5, input6 = int(ast.literal_eval(input.split()))
        problem.build_custom_table(1, 0, input4)
        problem.build_custom_table(1, 1, input5)
        problem.build_custom_table(1, 2, input6)

        # Ask user for third row
        print("Enter the third row, use space or tabs between numbers", end='')

        # Build third row
        input7, input8, input9 = int(ast.literal_eval(input.split()))
        problem.build_custom_table(2, 0, input7)
        problem.build_custom_table(2, 1, input8)
        problem.build_custom_table(2, 2, input9)

    # Select algorithm
    print("Enter your choice of algorithm")
    print("1: Uniform Cost Search")
    print("2: A* with the Misplaced Tile heuristic")
    print("3: A* with the Eucledian Distance heuristic")
    amode = ast.literal_eval(input())

    if amode == '1':
        s.uniform_cost(problem)
    elif amode == '2':
        s.astar_misplace_tile(problem)
    elif amode == '3':
        s.astar_euclidean_distance(problem)
