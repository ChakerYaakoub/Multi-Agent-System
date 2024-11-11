# behaviours.py
import random
from cells import FoodCell  # Import FoodCell directly since we need it here / Importer FoodCell directement car nous en avons besoin ici

class Behaviour:
    def execute(self, agent, environment):
        # Define a method to be overridden by subclasses / Définir une méthode à remplacer par les sous-classes
        pass

class ReproductionBehaviour(Behaviour):
    def execute(self, agent, environment):
        # Check if agent is a queen without importing Queen directly / Vérifier si l'agent est une reine sans importer Queen directement
        if agent.__class__.__name__ == "Queen":
            # 5% chance per step to spawn a new worker / 5% de chance par étape de faire apparaître un nouvel ouvrier
            if random.random() < 0.05:
                # Create a new worker through environment / Créer un nouvel ouvrier via l'environnement
                new_worker = environment.create_worker()
                # Start at queen's position / Commencer à la position de la reine
                new_worker.position = agent.position
                # Add the new worker to the environment / Ajouter le nouvel ouvrier à l'environnement
                environment.add_agent(new_worker)
                # Print message indicating a new worker has spawned / Imprimer un message indiquant qu'un nouvel ouvrier est apparu
                print("New worker spawned.")

class MovementBehaviour(Behaviour):
    def execute(self, agent, environment):
        # Random movement to simulate searching for food / Mouvement aléatoire pour simuler la recherche de nourriture
        if agent.__class__.__name__ == "Worker" and not agent.has_food:
            # Move in 4 possible directions / Se déplacer dans 4 directions possibles
            dx, dy = random.choice([(0, 1), (1, 0), (0, -1), (-1, 0)])
            new_x = agent.position[0] + dx
            new_y = agent.position[1] + dy

            # Ensure the worker stays within bounds / S'assurer que l'ouvrier reste dans les limites
            if 0 <= new_x < environment.width and 0 <= new_y < environment.height:
                # Update the worker's position / Mettre à jour la position de l'ouvrier
                agent.position = (new_x, new_y)

                # Check if the new position contains food / Vérifier si la nouvelle position contient de la nourriture
                if isinstance(environment.grid[new_y][new_x], FoodCell):
                    # Worker has found food / L'ouvrier a trouvé de la nourriture
                    agent.has_food = True
                    # Change color to red / Changer la couleur en rouge
                    agent.color = (255, 0, 0)
                    # Hide the food / Cacher la nourriture
                    environment.grid[new_y][new_x] = None
                    # Print message indicating food found / Imprimer un message indiquant que de la nourriture a été trouvée
                    print("Worker found food at:", agent.position)
            else:
                # Print message if worker tries to move out of bounds / Imprimer un message si l'ouvrier essaie de sortir des limites
                print("Worker attempted to move out of bounds.")

class BackToNestBehaviour(Behaviour):
    def execute(self, agent, environment):
        # Move towards the nest if carrying food / Se déplacer vers le nid si l'on transporte de la nourriture
        if agent.__class__.__name__ == "Worker" and agent.has_food:
            # Get the nest position / Obtenir la position du nid
            nest_position = environment.nest_position
            x, y = agent.position
            nest_x, nest_y = nest_position

            # Move one step towards the nest / Avancer d'un pas vers le nid
            dx = 1 if nest_x > x else -1 if nest_x < x else 0
            dy = 1 if nest_y > y else -1 if nest_y < y else 0
            # Update the worker's position / Mettre à jour la position de l'ouvrier
            agent.position = (x + dx, y + dy)

            # Check if the worker has returned to the nest / Vérifier si l'ouvrier est retourné au nid
            if agent.position == nest_position:
                # Ensure the worker is at the nest / S'assurer que l'ouvrier est au nid
                agent.position = nest_position
                # Drop off food / Déposer la nourriture
                agent.has_food = False
                # Change color back to blue / Repasser la couleur en bleu
                agent.color = (0, 0, 255)
                # Print message indicating return to nest / Imprimer un message indiquant le retour au nid
                print("Worker returned to nest with food.")
