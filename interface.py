# interface.py
import pygame
from environment import Environment
from cells import NestCell, FoodCell  # Importer NestCell et FoodCell ici

CELL_SIZE = 20
WIDTH, HEIGHT = 600, 600

class Interface:
    def __init__(self, environment):
        # Track last step time / Suivre le temps du dernier pas
        # Track last spawn time / Suivre le temps du dernier spawn
        # Initialize running attribute / Initialiser l'attribut de fonctionnement
        self.environment = environment
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Ant Farm Simulation")
        
        self.last_step_time = pygame.time.get_ticks()
        self.last_spawn_time = pygame.time.get_ticks()
        self.running = True

    def draw(self):
        # White background / Fond blanc
        self.screen.fill((255, 255, 255))

        # Draw grid cells (NestCell, FoodCell) / Dessiner les cellules de la grille (NestCell, FoodCell)
        for y in range(self.environment.height):
            for x in range(self.environment.width):
                cell = self.environment.grid[y][x]
                # Red for the nest / Rouge pour le nid
                # Green for food / Vert pour la nourriture
                # Light gray for empty / Gris clair pour vide
                if isinstance(cell, NestCell):
                    color = (255, 0, 0)
                elif isinstance(cell, FoodCell):
                    color = (0, 128, 0)  # A darker green color that is easier on the eyes
                else:
                    color = (200, 200, 200)

                pygame.draw.rect(
                    self.screen, color,
                    (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                )

        # Draw agents (Queen, Worker) / Dessiner les agents (Reine, Ouvrier)
        for agent in self.environment.agents:
            # Use the agent's color directly / Utiliser directement la couleur de l'agent
            ant_color = agent.color
            # pygame.draw.circle(
            #     self.screen, ant_color,
            #     (agent.position[0] * CELL_SIZE + CELL_SIZE // 2, agent.position[1] * CELL_SIZE + CELL_SIZE // 2),
            #     CELL_SIZE // 2  # Agent size (smaller circle within the cell) / Taille de l'agent (cercle plus petit dans la cellule)
            # )
            x_pos = agent.position[0] * CELL_SIZE
            y_pos = agent.position[1] * CELL_SIZE
           

            # Draw body parts: head, thorax, and abdomen
            pygame.draw.circle(self.screen, ant_color, (x_pos + CELL_SIZE // 2, y_pos + CELL_SIZE // 4), CELL_SIZE // 6)  # Head
            pygame.draw.circle(self.screen, ant_color, (x_pos + CELL_SIZE // 2, y_pos + CELL_SIZE // 2), CELL_SIZE // 5)  # Thorax
            pygame.draw.circle(self.screen, ant_color, (x_pos + CELL_SIZE // 2, y_pos + 3 * CELL_SIZE // 4), CELL_SIZE // 6)  # Abdomen

            # Draw legs using lines
            leg_length = CELL_SIZE // 4
            pygame.draw.line(self.screen, ant_color, (x_pos + CELL_SIZE // 4, y_pos + CELL_SIZE // 3), (x_pos, y_pos + CELL_SIZE // 4 + leg_length), 2)
            pygame.draw.line(self.screen, ant_color, (x_pos + 3 * CELL_SIZE // 4, y_pos + CELL_SIZE // 3), (x_pos + CELL_SIZE, y_pos + CELL_SIZE // 4 + leg_length), 2)
            pygame.draw.line(self.screen, ant_color, (x_pos + CELL_SIZE // 4, y_pos + 2 * CELL_SIZE // 3), (x_pos, y_pos + 3 * CELL_SIZE // 4), 2)
            pygame.draw.line(self.screen, ant_color, (x_pos + 3 * CELL_SIZE // 4, y_pos + 2 * CELL_SIZE // 3), (x_pos + CELL_SIZE, y_pos + 3 * CELL_SIZE // 4), 2)

         

        pygame.display.flip()

    def update(self):
        for event in pygame.event.get():
            # Set running to False on quit / Mettre running à False lors de la sortie
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                exit()
        
        # Check if the interface is not running / Vérifier si l'interface ne fonctionne pas
        if not self.running:
            # Draw that the game is over / Dessiner que le jeu est terminé
            font = pygame.font.Font(None, 36)
            text = font.render("All food has been collected", True, (0, 0, 0))
            # Center the text vertically / Centrer le texte verticalement
            text_rect = text.get_rect(center=(WIDTH // 2, 18 + 18))
            
            # Create a background rectangle that matches the text size / Créer un rectangle de fond qui correspond à la taille du texte
            # Inflate to add padding around the text / Gonfler pour ajouter un espace autour du texte
            # Change background color to red / Changer la couleur de fond en rouge
            background_rect = text_rect.inflate(20, 10)
            pygame.draw.rect(self.screen, (255, 0, 0), background_rect)
            
            # Use the centered text rect / Utiliser le rectangle de texte centré
            self.screen.blit(text, text_rect)
            pygame.display.flip()
            # Exit the update method to stop further processing / Quitter la méthode de mise à jour pour arrêter le traitement
            return

        # Get current time / Obtenir le temps actuel
        current_time = pygame.time.get_ticks()

        # Step the environment every 500 ms (0.5 seconds) / Faire avancer l'environnement toutes les 500 ms (0,5 secondes)
        if current_time - self.last_step_time >= 90:
            self.environment.step()
            # Update last step time / Mettre à jour le temps du dernier pas
            self.last_step_time = current_time

        # Spawn a new worker every 7 seconds / Faire apparaître un nouvel ouvrier toutes les 7 secondes
        if current_time - self.last_spawn_time >= 3000:
            # Create a new worker / Créer un nouvel ouvrier
            new_worker = self.environment.create_worker()
            self.environment.add_agent(new_worker)
            # Update last spawn time / Mettre à jour le temps du dernier spawn
            self.last_spawn_time = current_time

        # Draw the current state / Dessiner l'état actuel
        self.draw()
