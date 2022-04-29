import math
from typing_extensions import Self
import treenode as tn


# Define puzzle class
class Puzzle:
    # Data memebers
    num_row = 3
    num_col = 3
    blank_row = None
    blank_col = None
    initial_state = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, None]]
    goal_state_map = {
        '1' : [0, 0],
        '2' : [0, 1],
        '3' : [0, 2],
        '4' : [1, 0],
        '5' : [1, 1],
        '6' : [1, 2],
        '7' : [2, 1],
        '8' : [2, 2]
    }

    # Default Constructor
    def __init__(self) -> None:
        pass

    # Build puzzle using default table
    def build_default_table(self) -> None:
        self.initial_state = [[1, 2, 3], [4, 5, 6], [7, 8, None]]
        self.blank_row = 2
        self.blank_col = 2
        return

    # Build puzzle table using user input
    def build_custom_table(self, row, col, val) -> None:
        if row < self.num_row and col < self.num_col:
            if val == None:
                self.blank_row = row
                self.blank_col = col
            self.initial_state[row][col] = val
        return
    
    # Operator 1
    def move_blank_left(self, tnode : tn.TreeNode) -> bool:
        if tnode.blank_col > 0:
            tnode.state[tnode.blank_row][tnode.blank_col], tnode.state[tnode.blank_row][tnode.blank_col-1] = \
                tnode.state[tnode.blank_row][tnode.blank_col-1], tnode.state[tnode.blank_row][tnode.blank_col]
            tnode.blank_col -= 1
            return True
        return False

    # Operator 2
    def move_blank_right(self, tnode : tn.TreeNode) -> bool:
        if tnode.blank_col < self.num_col - 1:
            tnode.state[tnode.blank_row][tnode.blank_col], tnode.state[tnode.blank_row][tnode.blank_col+1] = \
                tnode.state[tnode.blank_row][tnode.blank_col+1], tnode.state[tnode.blank_row][tnode.blank_col]
            tnode.blank_col += 1
            return True
        return False
    
    # Operator 3
    def move_blank_up(self, tnode : tn.TreeNode) -> bool:
        if tnode.blank_row > 0:
            tnode.state[tnode.blank_row][tnode.blank_col], tnode.state[tnode.blank_row-1][tnode.blank_col] = \
                tnode.state[tnode.blank_row-1][tnode.blank_col], tnode.state[tnode.blank_row][tnode.blank_col]
            tnode.blank_row -= 1
            return True
        return False

    # Operator 4
    def move_blank_down(self, tnode : tn.TreeNode) -> bool:
        if tnode.blank_row < self.num_row - 1:
            tnode.state[tnode.blank_row][tnode.blank_col], tnode.state[tnode.blank_row+1][tnode.blank_col] = \
                tnode.state[tnode.blank_row+1][tnode.blank_col], tnode.state[tnode.blank_row][tnode.blank_col]
            tnode.blank_row += 1
            return True
        return False

    # Returns the number of misplaced tiles
    def find_misplaced_tile(self, tnode : tn.TreeNode) -> int:
        num_misplaced_tile = 0
        i = 1
        for tile in tnode.state:
            if i == 9:
                if tile != None:
                    num_misplaced_tile += 1
                    break
            if tile != i:
                num_misplaced_tile += 1
            i += 1
        return num_misplaced_tile

    # Find Euclidean distance between each tile's current position and its correct position
    def find_euclidean_distance(self, tnode : tn.TreeNode) -> float:
        euclidean_distance = 0
        row = 0
        col = 0
        for tile in tnode.state:
            if tile != None:
                euclidean_distance += math.sqrt(((row - self.goal_state_map[str(tile)][0]) ** 2) + ((col - \
                    self.goal_state_map[str(tile)][1])) ** 2)
            else:
                euclidean_distance += math.sqrt(((row - self.num_row + 1) ** 2) + ((col - self.num_col + 1) ** 2))
            if col < self.num_col - 1:
                col += 1
            else:
                col = 0
                row += 1
        return euclidean_distance


    # Might not be needed
    def swap(self, row1, col1, row2, col2) -> Self:
        if row1 >= self.num_row or row2 >= self.num_row:
            return
        if col1 >= self.num_col or row2 >= self.num_col:
            return
        self.current_state[row1][col1], self.current_state[row2][col2] = self.current_state[row2][col2], self.current_state[row1][col1]
        return