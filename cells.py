# cells.py

class Cell:
    def __init__(self, x, y):
        # Initialize the cell with x and y coordinates
        self.x = x
        self.y = y

class NestCell(Cell):
    # Represents a nest cell
    pass

class FoodCell(Cell):
    # Represents a food cell
    pass
