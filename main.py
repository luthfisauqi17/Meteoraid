import pygame
import random
import math

# Initialization 
pygame.init()

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

# Score
scoreValue = 0
font = pygame.font.Font("freesansbold.ttf", 32)
textX = 10
textY = 10


def showScore(x, y):
    score = font.render("Score: " + str(scoreValue), True, (255, 255, 255))
    screen.blit(score, (x, y))


# Characters
# Player
playerImg = pygame.image.load("assets/player.png")
playerX = 370
playerY = 480
playerXSpeed = 3
playerXChange = 0


def player(x, y):
    screen.blit(playerImg, (x, y))


# Target
targetImg = []
targetX = []
targetY = []
targetYChange = []
numOfTarget = 3

for i in range(numOfTarget):
    targetImg.append(pygame.image.load("assets/target.png"))
    targetX.append(random.randint(0, 735))
    targetY.append(random.randint(15, 50))
    targetYChange.append(2)


def target(x, y, i):
    screen.blit(targetImg[i], (x, y))


# Bullet
bulletImg = pygame.image.load("assets/bullet.png")
bulletX = 0
bulletY = playerY
bulletYChange = 3
bulletState = "ready"


def fireBullet(x, y):
    global bulletState
    bulletState = "fire"
    screen.blit(bulletImg, (x+16, y+10))


def isCollided(x1, y1, x2, y2):
    d = math.sqrt(math.pow(x2-x1, 2) + math.pow(y2-y1, 2))
    if d <= 27:
        return True
    else:
        return False


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
            if event.key == pygame.K_SPACE:
                if bulletState is "ready":
                    bulletX = playerX
                    fireBullet(bulletX, bulletY)

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

        bulletTargetCollision = isCollided(
            targetX[i], targetY[i], bulletX, bulletY)

        if bulletTargetCollision:
            bulletY = playerY
            bulletState = "ready"
            targetX[i] = random.randint(0, 735)
            targetY[i] = random.randint(25, 150)
            scoreValue += 1
            print(scoreValue)

        if targetY[i] >= 600:
            targetX[i] = random.randint(0, 735)
            targetY[i] = random.randint(15, 50)

        target(targetX[i], targetY[i], i)

    # Bullet move update
    if bulletY <= 0:
        bulletY = playerY
        bulletState = "ready"

    if bulletState is "fire":
        fireBullet(bulletX, bulletY)
        bulletY -= bulletYChange


    # Show score
    showScore(textX, textY)

    # Update screen
    pygame.display.update()
