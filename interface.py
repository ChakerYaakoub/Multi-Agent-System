# interface.py
import pygame
from environment import Environment
from cells import NestCell, FoodCell

CELL_SIZE = 20
WIDTH, HEIGHT = 600, 600


# //Create interface.py (Visual display):
class Interface:
    def __init__(self, environment):
        # Track last step time
        # Track last spawn time 
        # Initialize running attribute
        self.environment = environment
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Ant Farm Simulation")
        
        self.last_step_time = pygame.time.get_ticks()
        self.last_spawn_time = pygame.time.get_ticks()
        self.running = True

    def draw(self):
        # White background
        self.screen.fill((255, 255, 255))

        # Draw grid cells (NestCell, FoodCell)
        for y in range(self.environment.height):
            for x in range(self.environment.width):
                cell = self.environment.grid[y][x]
                # Red for the nest
                # Green for food
                # Light gray for empty
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

        # Draw agents (Queen, Worker)
        for agent in self.environment.agents:
            # Use the agent's color directly
            ant_color = agent.color
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
            # Set running to False on quit
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                exit()
        
        # Check if the interface is not running
        if not self.running:
            # Draw that the game is over
            font = pygame.font.Font(None, 36)
            text = font.render("All food has been collected", True, (0, 0, 0))
            # Center the text vertically
            text_rect = text.get_rect(center=(WIDTH // 2, 18 + 18))
            
            # Create a background rectangle that matches the text size
            # Inflate to add padding around the text
            # Change background color to red
            background_rect = text_rect.inflate(20, 10)
            pygame.draw.rect(self.screen, (255, 0, 0), background_rect)
            
            # Use the centered text rect
            self.screen.blit(text, text_rect)
            pygame.display.flip()
            # Exit the update method to stop further processing
            return

        # Get current time
        current_time = pygame.time.get_ticks()

        # Step the environment every 500 ms (0.5 seconds)
        if current_time - self.last_step_time >= 90:
            self.environment.step()
            # Update last step time
            self.last_step_time = current_time

        # Spawn a new worker every 7 seconds
        if current_time - self.last_spawn_time >= 3000:
            # Create a new worker
            new_worker = self.environment.create_worker()
            self.environment.add_agent(new_worker)
            # Update last spawn time
            self.last_spawn_time = current_time

        # Draw the current state
        self.draw()
