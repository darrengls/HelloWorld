"""
----------------------------------------
Title: Hello, World!
Author: Darren Gallois
Date: September 23, 2024
Description: This script creates a "Hello, World!" animation where the text
             bounces around the screen, changes color upon hitting the edges,
             and leaves a fading trail effect reminiscent of the classic DVD 
             screensaver. The text is outlined to reduce strain on the eyes
             and changes color more slowly to be less visually overwhelming.
----------------------------------------
"""

import pygame
import sys
import random

# Initialize Pygame and set up display parameters
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Hello, World!')

# Define font and colors
font = pygame.font.SysFont(None, 80)
trail_color = (15, 15, 15)  # Slightly dark to create the trail effect
outline_color = (0, 0, 0)   # Black outline color for better contrast

# Function to generate a random color
def random_color():
    return (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))

# Set initial position, velocity, and color of the text
text = "Hello, World!"
text_surface = font.render(text, True, random_color())
text_rect = text_surface.get_rect()
text_rect.topleft = (random.randint(0, width - text_rect.width), random.randint(0, height - text_rect.height))
velocity = [random.choice([-3, 3]), random.choice([-3, 3])]  # Reduced speed
color = random_color()  # Initial color
color_change_delay = 5  # Number of frames to wait before changing color again
color_change_counter = 0  # Counter to track when to change color

# Function to draw outlined text
def draw_outlined_text(surface, text, font, position, text_color, outline_color):
    # Render outline by drawing the text slightly offset in multiple directions
    outline_positions = [(position[0] + x, position[1] + y) for x in (-2, 0, 2) for y in (-2, 0, 2)]
    for pos in outline_positions:
        outline_surface = font.render(text, True, outline_color)
        surface.blit(outline_surface, pos)
    # Draw the main text on top
    main_surface = font.render(text, True, text_color)
    surface.blit(main_surface, position)

# Main loop for animation
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Create a fading trail effect
    screen.fill(trail_color, special_flags=pygame.BLEND_RGBA_SUB)

    # Bounce off walls and update color change counter
    if text_rect.left <= 0 or text_rect.right >= width:
        velocity[0] = -velocity[0]
        color_change_counter += 1
    if text_rect.top <= 0 or text_rect.bottom >= height:
        velocity[1] = -velocity[1]
        color_change_counter += 1

    # Change color only when the counter reaches the delay threshold
    if color_change_counter >= color_change_delay:
        color = random_color()
        text_surface = font.render(text, True, color)
        color_change_counter = 0  # Reset counter after changing color

    # Update text position
    text_rect = text_rect.move(velocity)

    # Draw outlined text
    draw_outlined_text(screen, text, font, text_rect.topleft, color, outline_color)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)
