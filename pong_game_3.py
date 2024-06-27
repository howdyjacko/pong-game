import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the game window
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Dragon Game')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Paddles and Ball
paddle_width, paddle_height = 10, 100
ball_size = 20
paddle1_x, paddle1_y = 50, screen_height // 2 - paddle_height // 2
paddle2_x, paddle2_y = screen_width - 50 - paddle_width, screen_height // 2 - paddle_height // 2
ball_x, ball_y = screen_width // 2 - ball_size // 2, screen_height // 2 - ball_size // 2

# Movement flags for paddles
left_paddle_up = False
left_paddle_down = False
right_paddle_up = False
right_paddle_down = False

# Game states
MENU = 0
PLAYING = 1
game_state = MENU

# Function to draw menu screen
def draw_menu():
    screen.fill(BLACK)
    font = pygame.font.Font(None, 36)
    instructions = [
        "Dragon Game Instructions:",
        " ",
        "Left Paddle Controls:",
        "  Q: Move Up",
        "  A: Move Down",
        " ",
        "Right Paddle Controls:",
        "  P: Move Up",
        "  L: Move Down",
        " ",
        "Press SPACE to Start"
    ]
    y_offset = 50
    for line in instructions:
        text = font.render(line, True, WHITE)
        text_rect = text.get_rect(center=(screen_width // 2, y_offset))
        screen.blit(text, text_rect)
        y_offset += 30

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_state == MENU:
                game_state = PLAYING
            elif event.key == pygame.K_q:
                left_paddle_up = True
            elif event.key == pygame.K_a:
                left_paddle_down = True
            elif event.key == pygame.K_p:
                right_paddle_up = True
            elif event.key == pygame.K_l:
                right_paddle_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_q:
                left_paddle_up = False
            elif event.key == pygame.K_a:
                left_paddle_down = False
            elif event.key == pygame.K_p:
                right_paddle_up = False
            elif event.key == pygame.K_l:
                right_paddle_down = False
    
    # Game logic based on state
    if game_state == PLAYING:
        # Handle paddle movement
        if left_paddle_up:
            paddle1_y -= 5
        elif left_paddle_down:
            paddle1_y += 5
        
        if right_paddle_up:
            paddle2_y -= 5
        elif right_paddle_down:
            paddle2_y += 5
        
        # Ensure paddles stay within screen bounds
        paddle1_y = max(0, min(screen_height - paddle_height, paddle1_y))
        paddle2_y = max(0, min(screen_height - paddle_height, paddle2_y))
        
        # Clear screen
        screen.fill(BLACK)
        
        # Draw paddles and ball
        pygame.draw.rect(screen, WHITE, (paddle1_x, paddle1_y, paddle_width, paddle_height))
        pygame.draw.rect(screen, WHITE, (paddle2_x, paddle2_y, paddle_width, paddle_height))
        pygame.draw.ellipse(screen, WHITE, (ball_x, ball_y, ball_size, ball_size))
        
    elif game_state == MENU:
        # Draw menu screen with instructions
        draw_menu()
    
    # Update display
    pygame.display.flip()
    
    # Control frame rate
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
