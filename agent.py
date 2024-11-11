# agent.py
from behaviours import ReproductionBehaviour, MovementBehaviour, BackToNestBehaviour

class Agent:
    def __init__(self, behaviours=[], color=(0, 0, 0)):
        # Initialize the agent with a list of behaviours and a color
        # Initialiser l'agent avec une liste de comportements et une couleur
        self.behaviours = behaviours
        self.position = (0, 0)  # Default starting position (to be set later) / Position de départ par défaut (à définir plus tard)
        self.color = color  # Set the agent's color / Définir la couleur de l'agent

    def add_behaviour(self, behaviour):
        # Add a new behaviour to the agent's list of behaviours
        # Ajouter un nouveau comportement à la liste des comportements de l'agent
        self.behaviours.append(behaviour)

class Queen(Agent):
    def __init__(self):
        # Initialize the Queen agent with specific behaviours and color
        # Initialiser l'agent Reine avec des comportements spécifiques et une couleur
        super().__init__(behaviours=[ReproductionBehaviour()], color=(255, 0, 255))

class Worker(Agent):
    def __init__(self):
        # Initialize the Worker agent with specific behaviours and color
        # Initialiser l'agent Ouvrier avec des comportements spécifiques et une couleur
        super().__init__(behaviours=[MovementBehaviour(), BackToNestBehaviour()], color=(0, 0, 255))
        self.has_food = False  # Track if the worker is carrying food / Suivre si l'ouvrier transporte de la nourriture
