import pygame
import sys

pygame.init()

window_size = (400, 200)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Hour Boost")

white = (255, 255, 255)
black = (0, 0, 0)

font = pygame.font.SysFont(None, 55)

text = font.render("Now Boosting!", True, white)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(black)

    text_rect = text.get_rect(center=(window_size[0] // 2, window_size[1] // 2))
    screen.blit(text, text_rect)

    pygame.display.flip()

# Pygame beenden
pygame.quit()
sys.exit()
