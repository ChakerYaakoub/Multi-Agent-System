# environment.py
from cells import NestCell, FoodCell
from agent import Queen, Worker  # Import Queen and Worker directly here

class Environment:
    def __init__(self, width, height):
        # Set the width of the environment / Définir la largeur de l'environnement
        self.width = width
        # Set the height of the environment / Définir la hauteur de l'environnement
        self.height = height
        # Create a grid initialized with None / Créer une grille initialisée avec None
        self.grid = [[None for _ in range(width)] for _ in range(height)]
        # Initialize an empty list for agents / Initialiser une liste vide pour les agents
        self.agents = []

        # Initialize environment with a nest in the center / Initialiser l'environnement avec un nid au centre
        # Calculate center position / Calculer la position centrale
        center_x, center_y = width // 2, height // 2
        # Place a nest cell at the center / Placer une cellule de nid au centre
        self.grid[center_y][center_x] = NestCell(center_x, center_y)
        # Store the nest position / Stocker la position du nid
        self.nest_position = (center_x, center_y)
        
        # Add queen to environment / Ajouter la reine à l'environnement
        # Create a Queen instance / Créer une instance de Reine
        self.queen = Queen()
        # Set the queen's position to the nest / Définir la position de la reine au nid
        self.queen.position = self.nest_position
        # Add the queen to the agents list / Ajouter la reine à la liste des agents
        self.agents.append(self.queen)

    def add_agent(self, agent):
        # Set the agent's position to the nest / Définir la position de l'agent au nid
        agent.position = self.nest_position
        # Add the agent to the agents list / Ajouter l'agent à la liste des agents
        self.agents.append(agent)

    def add_food(self, x, y):
        # Place a food cell at the specified position / Placer une cellule de nourriture à la position spécifiée
        self.grid[y][x] = FoodCell(x, y)

    def create_worker(self):
        # Create and return a new Worker instance / Créer et retourner une nouvelle instance de Worker
        return Worker()

    def step(self):
        # Execute each behaviour for all agents / Exécuter chaque comportement pour tous les agents
        for agent in self.agents:
            for behaviour in agent.behaviours:
                behaviour.execute(agent, self)
