# behaviours.py
import random
from cells import FoodCell  # Import FoodCell directly since we need it here

class Behaviour:
    def execute(self, agent, environment):
        # Define a method to be overridden by subclasses
        pass



class ReproductionBehaviour(Behaviour):
    def execute(self, agent, environment):
        # Check if agent is a queen without importing Queen directly
        if agent.__class__.__name__ == "Queen":
            # 5% chance per step to spawn a new worker
            if random.random() < 0.05:
                # Create a new worker through environment
                new_worker = environment.create_worker()
                # Start at queen's position
                new_worker.position = agent.position
                # Add the new worker to the environment
                environment.add_agent(new_worker)
                # Print message indicating a new worker has spawned
                print("New worker spawned.")

class MovementBehaviour(Behaviour):
    def execute(self, agent, environment):
        # Random movement to simulate searching for food
        if agent.__class__.__name__ == "Worker" and not agent.has_food:
            # Move in 4 possible directions
            dx, dy = random.choice([(0, 1), (1, 0), (0, -1), (-1, 0)])
            new_x = agent.position[0] + dx
            new_y = agent.position[1] + dy

            # Ensure the worker stays within bounds
            if 0 <= new_x < environment.width and 0 <= new_y < environment.height:
                # Update the worker's position
                agent.position = (new_x, new_y)

                # Check if the new position contains food
                if isinstance(environment.grid[new_y][new_x], FoodCell):
                    # Worker has found food
                    agent.has_food = True
                    # Change color to red
                    agent.color = (255, 0, 0)
                    # Hide the food
                    environment.grid[new_y][new_x] = None
                    # Print message indicating food found
                    print("Worker found food at:", agent.position)
            else:
                # Print message if worker tries to move out of bounds
                print("Worker attempted to move out of bounds.")

class BackToNestBehaviour(Behaviour):
    def execute(self, agent, environment):
        # Move towards the nest if carrying food
        if agent.__class__.__name__ == "Worker" and agent.has_food:
            # Get the nest position
            nest_position = environment.nest_position
            x, y = agent.position
            nest_x, nest_y = nest_position

            # Move one step towards the nest
            dx = 1 if nest_x > x else -1 if nest_x < x else 0
            dy = 1 if nest_y > y else -1 if nest_y < y else 0
            # Update the worker's position
            agent.position = (x + dx, y + dy)

            # Check if the worker has returned to the nest
            if agent.position == nest_position:
                # Ensure the worker is at the nest
                agent.position = nest_position
                # Drop off food
                agent.has_food = False
                # Change color back to blue
                agent.color = (0, 0, 255)
                # Print message indicating return to nest
                print("Worker returned to nest with food.")
