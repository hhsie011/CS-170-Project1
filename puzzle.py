import math
import treenode as tn
import copy

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
    def build_custom_table(self, row : int, col : int, val : int) -> None:
        if row < self.num_row and col < self.num_col:
            if val == 0:
                self.blank_row = row
                self.blank_col = col
                self.initial_state[row][col] = None
            else:
                self.initial_state[row][col] = val
        return

    # Goal test
    def goal_test(self, tnode : tn.TreeNode) -> bool:
        for gs, s in zip(self.goal_state, tnode.state):
            if (gs != s):
                return False
        return True
    
    # Operator 1
    def move_blank_left(self, tnode : tn.TreeNode) -> tn.TreeNode:
        temp = tn.TreeNode(tnode.state, tnode.blank_row, tnode.blank_col)
        temp.state[temp.blank_row][temp.blank_col] = temp.state[temp.blank_row][temp.blank_col - 1]
        temp.state[temp.blank_row][temp.blank_col - 1] = None
        temp.blank_col -= 1
        return temp

    # Operator 2
    def move_blank_right(self, tnode : tn.TreeNode) -> tn.TreeNode:
        temp = tn.TreeNode(tnode.state, tnode.blank_row, tnode.blank_col)
        temp.state[temp.blank_row][temp.blank_col] = temp.state[temp.blank_row][temp.blank_col + 1]
        temp.state[temp.blank_row][temp.blank_col + 1] = None
        temp.blank_col += 1
        return temp
    
    # Operator 3
    def move_blank_up(self, tnode : tn.TreeNode) -> tn.TreeNode:
        temp = tn.TreeNode(tnode.state, tnode.blank_row, tnode.blank_col)
        temp.state[temp.blank_row][temp.blank_col] = temp.state[temp.blank_row - 1][temp.blank_col]
        temp.state[temp.blank_row - 1][temp.blank_col] = None
        temp.blank_row -= 1
        return temp

    # Operator 4
    def move_blank_down(self, tnode : tn.TreeNode) -> tn.TreeNode:
        temp = tn.TreeNode(tnode.state, tnode.blank_row, tnode.blank_col)
        temp.state[temp.blank_row][temp.blank_col] = temp.state[temp.blank_row + 1][temp.blank_col]
        temp.state[temp.blank_row + 1][temp.blank_col] = None
        temp.blank_row += 1
        return temp

    # CHhck if we can move the blank tile left
    def check_blank_left(self, tnode : tn.TreeNode) -> bool:
        if tnode.blank_col > 0:
            return True
        else:
            return False
    
    # Check if we can move the blank tile right
    def check_blank_right(self, tnode : tn.TreeNode) -> bool:
        if tnode.blank_col < self.num_col - 1:
            return True
        else:
            return False

    # Check if we can move the blank tile up
    def check_blank_up(self, tnode : tn.TreeNode) -> bool:
        if tnode.blank_row > 0:
            return True
        else:
            return False

    # Check if we can move the blank tile down
    def check_blank_down(self, tnode : tn.TreeNode) -> bool:
        if tnode.blank_row < self.num_row - 1:
            return True
        else:
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


