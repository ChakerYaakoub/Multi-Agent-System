# environment.py
from cells import NestCell, FoodCell
from agent import Queen, Worker  # Import Queen and Worker directly here

class Environment:
    def __init__(self, width, height):
        # Set the width of the environment
        self.width = width
        # Set the height of the environment
        self.height = height
        # Create a grid initialized with None
        self.grid = [[None for _ in range(width)] for _ in range(height)]
        # Initialize an empty list for agents
        self.agents = []

        # Initialize environment with a nest in the center
        # Calculate center position
        center_x, center_y = width // 2, height // 2
        # Place a nest cell at the center
        self.grid[center_y][center_x] = NestCell(center_x, center_y)
        # Store the nest position
        self.nest_position = (center_x, center_y)
        
        # Add queen to environment
        # Create a Queen instance
        self.queen = Queen()
        # Set the queen's position to the nest
        self.queen.position = self.nest_position
        # Add the queen to the agents list
        self.agents.append(self.queen)

    def add_agent(self, agent):
        # Set the agent's position to the nest
        agent.position = self.nest_position
        # Add the agent to the agents list
        self.agents.append(agent)

    def add_food(self, x, y):
        # Place a food cell at the specified position
        self.grid[y][x] = FoodCell(x, y)

    def create_worker(self):
        # Create and return a new Worker instance
        return Worker()

    def step(self):
        # Execute each behaviour for all agents
        for agent in self.agents:
            for behaviour in agent.behaviours:
                behaviour.execute(agent, self)
