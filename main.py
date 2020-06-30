import pygame

# Window size
(width, height) = (800, 600)

# Game screen
screen = pygame.display.set_mode((width, height))

# Set window title
pygame.display.set_caption("Meteoraid")

# Set window game icon
gameIcon = pygame.image.load("assets/icon.png")
pygame.display.set_icon(gameIcon)

# Characters
# Player
playerImg = pygame.image.load("assets/player.png")
playerX = 370
playerY = 480

# Functions
# Player


def player(x, y):
    screen.blit(playerImg, (x, y))


# Loop
running = True
while running:

    # Background
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player(playerX, playerY)

    # Update screen
    pygame.display.update()
