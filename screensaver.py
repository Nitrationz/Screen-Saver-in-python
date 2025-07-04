import time
import pygame
import random

WIDTH, HEIGHT = 1920, 1080
pygame.init()
display = pygame.display.set_mode((WIDTH, HEIGHT))
caption = pygame.display.set_caption("Screen Saver in Python")
pygame.display.flip()
BG = pygame.image.load("bg.jpg")


def draw():
    display.blit(BG,(0, 0))
    pygame.display.update()

draw()



def main():
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
    pygame.quit()

if __name__ == "__main__":
    main()