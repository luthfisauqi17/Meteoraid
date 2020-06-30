import pygame
import random

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

# Target
targetImg = pygame.image.load("assets/target.png")
targetX = random.randint(0,735)
targetY = random.randint(50, 150)
targetYChange = 1


# Functions
# Player


def player(x, y):
  screen.blit(playerImg, (x, y))

def target(x, y):
  screen.blit(targetImg, (x, y))


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

    if playerX <= 0:
      playerX = 0
    elif playerX >= 736:
      playerX = 736

    player(playerX, playerY)

    # Target move update
    targetY += targetYChange
    target(targetX, targetY)

    # Update screen
    pygame.display.update()
