import pygame
import random

# Window size
(width, height) = (800, 600)

# Game screen
screen = pygame.display.set_mode((width, height))

# Background
background = pygame.image.load("assets/background.png")

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
playerXSpeed = 3
playerXChange = 0

# Target
targetImg = []
targetX = []
targetY = []
targetYChange = []
numOfTarget = 3

for i in range(numOfTarget):
    targetImg.append(pygame.image.load("assets/target.png"))
    targetX.append(random.randint(0, 735))
    targetY.append(random.randint(25, 150))
    targetYChange.append(2)


# Functions
# Player


def player(x, y):
    screen.blit(playerImg, (x, y))


def target(x, y, i):
    screen.blit(targetImg[i], (x, y))


# Loop
running = True
while running:

    # Background
    screen.blit(background, (0, 0))

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

    for i in range(numOfTarget):
        targetY[i] += targetYChange[i]

        if targetY[i] >= 600:
            targetX[i] = random.randint(0, 735)
            targetY[i] = random.randint(25, 150)

        target(targetX[i], targetY[i], i)

    # Update screen
    pygame.display.update()
