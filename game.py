import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 600, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Interactive Bouncing Ball")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Function to generate a random color
def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Ball properties
ball_radius = 30
ball_x = random.randint(ball_radius, width - ball_radius)
ball_y = random.randint(ball_radius, height - ball_radius)
ball_speed_x = random.choice([-4, 4])
ball_speed_y = random.choice([-4, 4])
ball_color = random_color()

# Score and timer
score = 0
start_time = time.time()
game_duration = 20  # seconds

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the ball is clicked
            mouse_x, mouse_y = event.pos
            if (mouse_x - ball_x) ** 2 + (mouse_y - ball_y) ** 2 <= ball_radius ** 2:
                score += 1  # Increment score
                ball_color = random_color()  # Change color
                ball_radius = random.randint(20, 60)  # Change size

    # Update ball position
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Bounce the ball off the walls
    if ball_x - ball_radius <= 0 or ball_x + ball_radius >= width:
        ball_speed_x = -ball_speed_x
    if ball_y - ball_radius <= 0 or ball_y + ball_radius >= height:
        ball_speed_y = -ball_speed_y

    # Fill the background
    screen.fill(WHITE)

    # Draw the ball
    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)

    # Display score
    font = pygame.font.Font(None, 36)
    score_text = font.render(f'Score: {score}', True, BLACK)
    screen.blit(score_text, (10, 10))

    # Check if time is up
    if time.time() - start_time > game_duration:
        running = False
        break

    # Update the display
    pygame.display.flip()

    # Frame rate
    pygame.time.Clock().tick(60)

# Game Over Screen
screen.fill(WHITE)
font = pygame.font.Font(None, 74)
game_over_text = font.render('Game Over!', True, BLACK)
final_score_text = font.render(f'Final Score: {score}', True, BLACK)
screen.blit(game_over_text, (width // 2 - 150, height // 2 - 50))
screen.blit(final_score_text, (width // 2 - 150, height // 2 + 20))
pygame.display.flip()
pygame.time.delay(3000)

# Quit Pygame
pygame.quit()
