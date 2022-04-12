import array

# Define puzzle class
class Puzzle:
    num_col = 3
    first_row = array.array([0, 0 , 0])
    second_row = array.array([0, 0, 0])
    third_row = array.array([0, 0, 0])

    def swap(self, row1, col1, row2, col2):
        temp = None
        if row1 == 0:
            if col1 < len(self.num_col):
                temp = self.first_row[col1]
            else:
                return
        elif row1 == 1:
            if col1 < len(self.num_col):
                temp = self.second_row[col1]
            else:
                return
        elif row1 == 2:
            if col1 < len(self.num_col):
                temp = self.third_row[col1]
            else:
                return
        return