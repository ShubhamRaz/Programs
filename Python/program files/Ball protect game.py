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
stick_y = HEIGHT - STICK_HEIGHT - 50  # Move the stick up from the bottom

# Initial velocity of the ball
ball_dx = 5
ball_dy = 5

# Game state
game_over = False
score = 0  # Score instead of Bounces
high_score = 0

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if game_over and event.key == pygame.K_r:
                # Restart the game
                game_over = False
                ball_x = (WIDTH - BALL_RADIUS) // 2
                ball_y = 50
                stick_x = (WIDTH - STICK_WIDTH) // 2
                stick_y = HEIGHT - STICK_HEIGHT - 50
                ball_dx = 5
                ball_dy = 5
                score = 0

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
            score += 1
            if score > high_score:
                high_score = score

        # Check if the ball reaches the bottom
        if ball_y >= HEIGHT:
            game_over = True

        # Draw the stick
        pygame.draw.rect(screen, STICK_COLOR, (stick_x, stick_y, STICK_WIDTH, STICK_HEIGHT))

        # Draw the ball
        pygame.draw.circle(screen, BALL_COLOR, (ball_x, ball_y), BALL_RADIUS)

        # Draw a horizontal border line between stick and score
        pygame.draw.line(screen, STICK_COLOR, (0, stick_y + STICK_HEIGHT), (WIDTH, stick_y + STICK_HEIGHT))

        # Draw the score below the line
        score_text = font.render(f"Score: {score}", True, TEXT_COLOR)
        score_rect = score_text.get_rect(center=(WIDTH // 2, stick_y + STICK_HEIGHT + 20))
        screen.blit(score_text, score_rect)

        # Draw the high score to the right of the score
        high_score_text = font.render(f"High Score: {high_score}", True, TEXT_COLOR)
        high_score_rect = high_score_text.get_rect(center=(3 * WIDTH // 4, stick_y + STICK_HEIGHT + 20))
        screen.blit(high_score_text, high_score_rect)

    else:
        # Display "Game Over" message
        text = font.render("Game Over", True, TEXT_COLOR)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text, text_rect)
        restart_text = font.render("Press 'R' to Restart", True, TEXT_COLOR)
        restart_rect = restart_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 60))
        screen.blit(restart_text, restart_rect)

    # Update the display
    pygame.display.flip()

    # Control frame rate
    pygame.time.delay(30)

# Quit Pygame
pygame.quit()
sys.exit()
