# main.py
import random
from agent import Worker
from cells import FoodCell
from environment import Environment
from interface import Interface


# the video is here:
# https://edit.screencastify.com/edit

#  diagram :
# https://www.planttext.com/

# Finally, create main.py (Runs everything):

def main():
    width, height = 30, 30 
    environment = Environment(width, height)
    
    # Add 10 random food cells
    for _ in range(10):
        while True:
            x = random.randint(0, width - 1)
            y = random.randint(0, height - 1)
            # Ensure food is not placed at the queen's position
            if (x, y) != environment.nest_position:
                environment.add_food(x, y)
                break

    # Create and run interface
    interface = Interface(environment)
    while True:
        interface.update()
        
        # Check if all food is eaten
        if all(cell is None for row in environment.grid for cell in row if isinstance(cell, FoodCell)):
            if all(not isinstance(agent, Worker) or not agent.has_food for agent in environment.agents):
                print("All food has been collected.")
                interface.running = False

if __name__ == "__main__":
    main()
