import puzzle as p

# Define Node Class
class TreeNode:
    # Data members
    state = []
    blank_row = None
    blank_col = None

    # Constructor
    def __init__(self, current_state : list, row : int, col : int) -> None:
        self.state = current_state
        self.blank_row = row
        self.blank_col = col
