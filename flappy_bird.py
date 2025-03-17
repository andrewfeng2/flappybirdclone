import pygame
import random
import sys
import math

# Initialize pygame
pygame.init()

# Game constants
WIDTH, HEIGHT = 400, 600
FPS = 60
GRAVITY = 0.25
FLAP_STRENGTH = -7
PIPE_SPEED = 3
PIPE_SPAWN_RATE = 1500  # milliseconds
PIPE_GAP = 150
GROUND_HEIGHT = 100

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 128, 0)
BLUE = (0, 0, 255)
SKY_BLUE = (135, 206, 235)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
RED = (255, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird Clone")
clock = pygame.time.Clock()

# Create bird sprite
def create_bird_sprite():
    # Create a surface for the bird with transparency
    bird_surface = pygame.Surface((40, 30), pygame.SRCALPHA)
    
    # Draw the bird body (yellow circle)
    pygame.draw.circle(bird_surface, YELLOW, (20, 15), 15)
    
    # Draw the bird's eye (white with black pupil)
    pygame.draw.circle(bird_surface, WHITE, (28, 10), 5)
    pygame.draw.circle(bird_surface, BLACK, (30, 10), 2)
    
    # Draw the bird's beak (orange triangle)
    pygame.draw.polygon(bird_surface, ORANGE, [(35, 15), (45, 12), (35, 18)])
    
    # Draw the bird's wing
    pygame.draw.ellipse(bird_surface, (220, 220, 0), (10, 15, 20, 10))
    
    return bird_surface

# Load images
bird_img = create_bird_sprite()
pipe_img = pygame.Surface((60, HEIGHT))
pipe_img.fill(GREEN)
ground_img = pygame.Surface((WIDTH, GROUND_HEIGHT))
ground_img.fill((139, 69, 19))  # Brown

# Game classes
class Bird:
    def __init__(self):
        self.x = 100
        self.y = HEIGHT // 2
        self.velocity = 0
        self.rect = pygame.Rect(self.x, self.y, 34, 24)  # Slightly smaller than the image
        self.alive = True
        self.flap_animation = 0
        self.wing_up = False
    
    def flap(self):
        self.velocity = FLAP_STRENGTH
        self.wing_up = True
        self.flap_animation = 5  # Animation frames
    
    def update(self):
        # Apply gravity
        self.velocity += GRAVITY
        self.y += self.velocity
        
        # Update rect position (centered on the bird image)
        self.rect.x = self.x
        self.rect.y = self.y
        
        # Update flap animation
        if self.flap_animation > 0:
            self.flap_animation -= 1
        else:
            self.wing_up = False
        
        # Check if bird hits the ground or ceiling
        if self.rect.bottom >= HEIGHT - GROUND_HEIGHT or self.rect.top <= 0:
            self.alive = False

    def draw(self):
        # Create a copy of the bird image for rotation and wing animation
        bird_copy = bird_img.copy()
        
        # Animate the wing by drawing over the original wing
        if self.wing_up:
            # Draw wing in up position
            pygame.draw.ellipse(bird_copy, (220, 220, 0), (10, 8, 20, 10))
        
        # Calculate rotation based on velocity (capped to avoid extreme angles)
        angle = max(-30, min(30, -self.velocity * 2))
        
        # Rotate the bird
        rotated_bird = pygame.transform.rotate(bird_copy, angle)
        
        # Get the rect for the rotated image to ensure it's centered properly
        rotated_rect = rotated_bird.get_rect(center=self.rect.center)
        
        # Draw the bird
        screen.blit(rotated_bird, rotated_rect.topleft)

class Pipe:
    def __init__(self):
        self.gap_y = random.randint(150, HEIGHT - GROUND_HEIGHT - 150)
        self.x = WIDTH
        self.passed = False
        
        # Create top and bottom pipe rects
        self.top_rect = pygame.Rect(self.x, 0, 60, self.gap_y - PIPE_GAP // 2)
        self.bottom_rect = pygame.Rect(
            self.x, 
            self.gap_y + PIPE_GAP // 2, 
            60, 
            HEIGHT - (self.gap_y + PIPE_GAP // 2) - GROUND_HEIGHT
        )
    
    def update(self):
        self.x -= PIPE_SPEED
        self.top_rect.x = self.x
        self.bottom_rect.x = self.x
    
    def draw(self):
        # Draw top pipe (flipped)
        top_pipe = pygame.transform.flip(pipe_img, False, True)
        top_pipe = pygame.transform.scale(top_pipe, (60, self.top_rect.height))
        screen.blit(top_pipe, self.top_rect)
        
        # Draw bottom pipe
        bottom_pipe = pygame.transform.scale(pipe_img, (60, self.bottom_rect.height))
        screen.blit(bottom_pipe, self.bottom_rect)

class Game:
    def __init__(self):
        self.bird = Bird()
        self.pipes = []
        self.score = 0
        self.last_pipe_time = pygame.time.get_ticks()
        self.game_over = False
        self.game_started = False
        self.font = pygame.font.SysFont(None, 36)
        self.high_score = 0
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not self.game_started:
                        self.game_started = True
                    elif not self.game_over:
                        self.bird.flap()
                    else:
                        # Update high score before resetting
                        self.high_score = max(self.high_score, self.score)
                        self.__init__()  # Reset game
                        self.game_started = True  # Start immediately on restart
    
    def update(self):
        if not self.game_started or self.game_over:
            return
            
        # Update bird
        self.bird.update()
        
        # Check if it's time to spawn a new pipe
        current_time = pygame.time.get_ticks()
        if current_time - self.last_pipe_time > PIPE_SPAWN_RATE:
            self.pipes.append(Pipe())
            self.last_pipe_time = current_time
        
        # Update pipes and check for collisions
        for pipe in self.pipes[:]:
            pipe.update()
            
            # Check for collision with bird
            if pipe.top_rect.colliderect(self.bird.rect) or pipe.bottom_rect.colliderect(self.bird.rect):
                self.bird.alive = False
            
            # Check if bird passed the pipe
            if not pipe.passed and pipe.x + 60 < self.bird.x:
                pipe.passed = True
                self.score += 1
            
            # Remove pipes that are off screen
            if pipe.x < -60:
                self.pipes.remove(pipe)
        
        # Check if bird is alive
        if not self.bird.alive:
            self.game_over = True
            # Update high score
            self.high_score = max(self.high_score, self.score)
    
    def draw(self):
        # Draw background
        screen.fill(SKY_BLUE)
        
        # Draw clouds (simple decoration)
        for i in range(3):
            cloud_x = (WIDTH * i // 3 + (pygame.time.get_ticks() // 100) % WIDTH) % WIDTH
            cloud_y = 100 + i * 50
            pygame.draw.circle(screen, WHITE, (cloud_x, cloud_y), 20)
            pygame.draw.circle(screen, WHITE, (cloud_x + 15, cloud_y - 10), 15)
            pygame.draw.circle(screen, WHITE, (cloud_x + 15, cloud_y + 10), 15)
            pygame.draw.circle(screen, WHITE, (cloud_x + 30, cloud_y), 20)
        
        # Draw pipes
        for pipe in self.pipes:
            pipe.draw()
        
        # Draw ground
        screen.blit(ground_img, (0, HEIGHT - GROUND_HEIGHT))
        
        # Draw grass on top of ground
        for i in range(WIDTH // 10):
            grass_height = random.randint(5, 10)
            pygame.draw.line(screen, (0, 150, 0), 
                            (i * 10, HEIGHT - GROUND_HEIGHT),
                            (i * 10, HEIGHT - GROUND_HEIGHT - grass_height), 2)
        
        # Only draw the game bird if the game has started
        if self.game_started or self.game_over:
            self.bird.draw()
        
        # Draw score
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        screen.blit(score_text, (10, 10))
        
        # Draw high score
        if self.high_score > 0:
            high_score_text = self.font.render(f"Best: {self.high_score}", True, WHITE)
            screen.blit(high_score_text, (WIDTH - high_score_text.get_width() - 10, 10))
        
        # Draw game over or start message
        if self.game_over:
            # Semi-transparent overlay
            overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 128))
            screen.blit(overlay, (0, 0))
            
            game_over_text = self.font.render("Game Over!", True, WHITE)
            screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - 50))
            
            restart_text = self.font.render("Press SPACE to restart", True, WHITE)
            screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2))
            
            score_text = self.font.render(f"Score: {self.score}", True, WHITE)
            screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2 + 50))
            
        elif not self.game_started:
            # Draw title and animated bird on start screen
            title_text = self.font.render("FLAPPY BIRD", True, WHITE)
            screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 3))
            
            start_text = self.font.render("Press SPACE to start", True, WHITE)
            screen.blit(start_text, (WIDTH // 2 - start_text.get_width() // 2, HEIGHT // 2))
            
            # Draw animated bird on title screen (using the game bird's position)
            title_bird = create_bird_sprite()
            flap_offset = math.sin(pygame.time.get_ticks() / 200) * 5
            screen.blit(title_bird, (WIDTH // 2 - 20, HEIGHT // 2 - 100 + flap_offset))

# Main game loop
def main():
    game = Game()
    
    while True:
        game.handle_events()
        game.update()
        game.draw()
        
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
