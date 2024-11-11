# cells.py

class Cell:
    def __init__(self, x, y):
        # Initialize the cell with x and y coordinates
        # Initialiser la cellule avec les coordonnées x et y
        self.x = x
        self.y = y

class NestCell(Cell):
    # Represents a nest cell
    # Représente une cellule de nid
    pass

class FoodCell(Cell):
    # Represents a food cell
    # Représente une cellule de nourriture
    pass
