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

# Loop
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False