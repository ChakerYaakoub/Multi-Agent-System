# agent.py
from behaviours import ReproductionBehaviour, MovementBehaviour, BackToNestBehaviour


# Next, create agent.py (Define ant types):
class Agent:
    def __init__(self, behaviours=[], color=(0, 0, 0)):
        # Initialize the agent with a list of behaviours and a color
        self.behaviours = behaviours
        self.position = (0, 0)  # Default starting position (to be set later)
        self.color = color  # Set the agent's color

    def add_behaviour(self, behaviour):
        # Add a new behaviour to the agent's list of behaviours
        self.behaviours.append(behaviour)

class Queen(Agent):
    def __init__(self):
        # Initialize the Queen agent with specific behaviours and color
        super().__init__(behaviours=[ReproductionBehaviour()], color=(255, 0, 255))

class Worker(Agent):
    def __init__(self):
        # Initialize the Worker agent with specific behaviours and color
        super().__init__(behaviours=[MovementBehaviour(), BackToNestBehaviour()], color=(0, 0, 255))
        self.has_food = False  # Track if the worker is carrying food
