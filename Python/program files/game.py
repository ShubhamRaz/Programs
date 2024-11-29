import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (255, 255, 255)
BALL_COLOR = (0, 0, 255)
STICK_COLOR = (255, 0, 0)
TEXT_COLOR = (255, 0, 0)
BALL_RADIUS = 20
STICK_WIDTH, STICK_HEIGHT = 100, 10
STICK_SPEED = 10
FONT_SIZE = 48

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Ball Protection Game')

# Initialize font
font = pygame.font.Font(None, FONT_SIZE)

# Initial position of the ball
ball_x = (WIDTH - BALL_RADIUS) // 2
ball_y = 50

# Initial position of the stick
stick_x = (WIDTH - STICK_WIDTH) // 2
stick_y = HEIGHT - 20

# Initial velocity of the ball
ball_dx = 5
ball_dy = 5

# Game state
game_over = False

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        # Clear the screen
        screen.fill(BACKGROUND_COLOR)

        # Move the stick based on user input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and stick_x > 0:
            stick_x -= STICK_SPEED
        if keys[pygame.K_RIGHT] and stick_x < WIDTH - STICK_WIDTH:
            stick_x += STICK_SPEED

        # Update ball position
        ball_x += ball_dx
        ball_y += ball_dy

        # Check collision with walls
        if ball_x - BALL_RADIUS <= 0 or ball_x + BALL_RADIUS >= WIDTH:
            ball_dx *= -1

        if ball_y - BALL_RADIUS <= 0:
            ball_dy *= -1

        # Check collision with stick
        if (
            ball_y + BALL_RADIUS >= stick_y
            and ball_x >= stick_x
            and ball_x <= stick_x + STICK_WIDTH
            and ball_dy > 0
        ):
            ball_dy *= -1

        # Check if the ball reaches the bottom
        if ball_y >= HEIGHT:
            game_over = True

        # Draw the stick
        pygame.draw.rect(screen, STICK_COLOR, (stick_x, stick_y, STICK_WIDTH, STICK_HEIGHT))

        # Draw the ball
        pygame.draw.circle(screen, BALL_COLOR, (ball_x, ball_y), BALL_RADIUS)
    else:
        # Display "Game Over" message
        text = font.render("Game Over", True, TEXT_COLOR)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text, text_rect)

    # Update the display
    pygame.display.flip()

    # Control frame rate
    pygame.time.delay(30)

# Quit Pygame
pygame.quit()
sys.exit()
