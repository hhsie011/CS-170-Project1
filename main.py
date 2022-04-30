#170 project 1
import ast
import puzzle as p
import search as s


# Create default puzzle
if __name__ == "__main__":
    # Welcome message
    print("Welcome to 862073206 8 puzzle solver.\n")

    # Ask user how to build puzzle
    pmode = input("Type \"1\" to use a default puzzle, or \"2\" to enter your own puzzle. ")
    print('\n')
    
    # Instantitate a puzzle object
    problem = p.Puzzle()

    # Default puzzle
    if pmode == '1':
        problem.build_default_table()
    # Custom puzzle
    elif pmode == '2':
        print("Enter your puzzle, use a zero to represent the blank")

        # Ask user for first row
        input1, input2, input3 = input("Enter the frist row, use space or tabs between numbers ").split()

        # Build first row
        problem.build_custom_table(0, 0, int(input1))
        problem.build_custom_table(0, 1, int(input2))
        problem.build_custom_table(0, 2, int(input3))

        # Ask user for second row
        input4, input5, input6 = input("Enter the second row, use space or tabs between numbers ").split()

        # Build second row
        problem.build_custom_table(1, 0, int(input4))
        problem.build_custom_table(1, 1, int(input5))
        problem.build_custom_table(1, 2, int(input6))

        # Ask user for third row
        input7, input8, input9 = input("Enter the third row, use space or tabs between numbers ").split()

        # Build third row
        problem.build_custom_table(2, 0, int(input7))
        problem.build_custom_table(2, 1, int(input8))
        problem.build_custom_table(2, 2, int(input9))

    # Select algorithm
    print("\nEnter your choice of algorithm")
    print("1: Uniform Cost Search")
    print("2: A* with the Misplaced Tile heuristic")
    print("3: A* with the Eucledian Distance heuristic")
    amode = input()
    print('\n')

    if amode == '1':
        solution_found, num_nodes_expanded, max_queue_size, solution_cost = s.uniform_cost(problem)
        if solution_found == 1:
            print("We found a solution!!!")
        else:
            print("We did not find a solution :(")
        print("We expanded ", num_nodes_expanded, " nodes")
        print("The maximum queue size was ", max_queue_size)
        print("The solution had a cost of ", solution_cost)
    elif amode == '2':
        s.astar_misplace_tile(problem)
    elif amode == '3':
        s.astar_euclidean_distance(problem)
