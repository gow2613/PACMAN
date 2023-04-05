import pygame
import sys

# Game constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BOARD_WIDTH = 20
BOARD_HEIGHT = 15
BLOCK_SIZE = 40
PACMAN_SPEED = 5
GHOST_SPEED = 3
COIN_COLOR = (255, 255, 0)
PACMAN_COLOR = (255, 255, 0)
GHOST_COLOR = (255, 0, 0)
WALL_COLOR = (0, 0, 255)
BACKGROUND_COLOR = (0, 0, 0)
LEVELS = [
    [
        "####################",
        "#C#C#C#C#C#C#C#C#C#C#",
        "#C#C#C#C#C#C#C#C#C#C#",
        "#C#C#C#C#C#C#C#C#C#C#",
        "#C#C#C#C#C#C#C#C#C#C#",
        "#C#C#C#C#C#C#C#C#C#C#",
        "#C#C#C#C#C#C#C#C#C#C#",
        "#C#C#C#C#C#C#C#C#C#C#",
        "#C#C#C#C#C#C#C#C#C#C#",
        "#C#C#C#C#C#C#C#C#C#C#",
        "#C#C#C#C#C#C#C#C#C#C#",
        "#C#C#C#C#C#C#C#C#C#C#",
        "#C#C#C#C#C#C#C#C#C#C#",
        "####################"
    ],
    # Add more levels here...
]

# Game state
current_level = 0
pacman_pos = [0, 0]
ghost_pos = [BOARD_WIDTH - 1, BOARD_HEIGHT - 1]
coins_pos = []
walls_pos = []

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pac-Man")

def draw_board():
    # Draw background
    screen.fill(BACKGROUND_COLOR)
    
    # Draw walls
    for wall in walls_pos:
        pygame.draw.rect(screen, WALL_COLOR, pygame.Rect(wall[0] * BLOCK_SIZE, wall[1] * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
    
    # Draw coins
    for coin in coins_pos:
        pygame.draw.circle(screen, COIN_COLOR, (coin[0] * BLOCK_SIZE + BLOCK_SIZE // 2, coin[1] * BLOCK_SIZE + BLOCK_SIZE // 2), BLOCK_SIZE // 10)

    # Draw Pac-Man
    pygame.draw.circle(screen, PACMAN_COLOR, (pacman_pos[0] * BLOCK_SIZE + BLOCK_SIZE // 2, pacman_pos[1] * BLOCK_SIZE + BLOCK_SIZE // 2), BLOCK_SIZE // 2)

    # Draw Ghost
    pygame.draw.circle(screen, GHOST_COLOR, (ghost_pos[0] * BLOCK_SIZE + BLOCK_SIZE //
