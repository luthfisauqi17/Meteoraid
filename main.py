import pygame

# Window size
(width, height) = (800, 600)

# Game screen
screen = pygame.display.set_mode((width, height))

# Window title
pygame.display.set_caption("Meteoraid")

# Loop
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False