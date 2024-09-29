import pygame
from constants import *
from player import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps = pygame.time.Clock()
    dt = 0
    p1 = Player(SCREEN_WIDTH /2, SCREEN_HEIGHT /2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        p1.update(dt)
        screen.fill("black")
        
        p1.draw(screen)
        pygame.display.flip()
        fps.tick(60)













if __name__ == "__main__":
    main()