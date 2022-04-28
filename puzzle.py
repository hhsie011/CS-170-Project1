import array

# Define puzzle class
class Puzzle:
    # Data memebers
    num_row = 3
    num_col = 3
    blank_row = None
    blank_col = None
    initial_state = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    table = [[0, 0, 0,], [0, 0, 0], [0, 0, 0]]
    goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, None]]

    # Build puzzle table using user input
    def build_custom_table(self, row, col, val):
        if row < self.num_row and col < self.num_col:
            self.initial_state[row][col] = val
            self.table[row][col] = self.initial_state[row][col]
        return
    
    # Operator 1
    def move_blank_left(self):
        if self.blank_col > 0:
            self.table[self.blank_row][self.blank_col], self.table[self.blank_row][self.blank_col-1] = \
                self.table[self.blank_row][self.blank_col-1], self.table[self.blank_row][self.blank_col]
            self.blank_col -= 1
        return

    # Operator 2
    def move_blank_right(self):
        if self.blank_col < self.num_col - 1:
            self.table[self.blank_row][self.blank_col], self.table[self.blank_row][self.blank_col+1] = \
                self.table[self.blank_row][self.blank_col+1], self.table[self.blank_row][self.blank_col]
            self.blank_col += 1
        return
    
    # Operator 3
    def move_blank_up(self):
        if self.blank_row > 0:
            self.table[self.blank_row][self.blank_col], self.table[self.blank_row-1][self.blank_col] = \
                self.table[self.blank_row-1][self.blank_col], self.table[self.blank_row][self.blank_col]
            self.blank_row -= 1
        return

    # Operator 4
    def move_blank_down(self):
        if self.blank_row < self.num_row - 1:
            self.table[self.blank_row][self.blank_col], self.table[self.blank_row+1][self.blank_col] = \
                self.table[self.blank_row+1][self.blank_col], self.table[self.blank_row][self.blank_col]
            self.blank_row += 1
        return

    def swap(self, row1, col1, row2, col2):
        if row1 >= self.num_row or row2 >= self.num_row:
            return
        if col1 >= self.num_col or row2 >= self.num_col:
            return
        self.table[row1][col1], self.table[row2][col2] = self.table[row2][col2], self.table[row1][col1]
        return