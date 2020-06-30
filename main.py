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
playerXSpeed = 1
playerXChange = 0

# Functions
# Player


def player(x, y):
    screen.blit(playerImg, (x, y))


# Loop
running = True
while running:

    # Background
    screen.fill((0, 0, 0))

    # Events handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Keyboard control stroke
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_LEFT:
            playerXChange = -playerXSpeed
          if event.key == pygame.K_RIGHT:
            playerXChange = playerXSpeed
          
        if event.type == pygame.KEYUP:
          if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            playerXChange = 0

    # Player move update
    playerX += playerXChange
    player(playerX, playerY)

    # Update screen
    pygame.display.update()
