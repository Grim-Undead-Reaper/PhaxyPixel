import pygame, sys
from Constants import *

window = pygame.display.set_mode((WIDTH, HEIGHT))

run = True

while run:
  
  window.fill(COLOR["WHITE"])

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
      pygame.quit()
      sys.exit()

    pygame.display.flip()
