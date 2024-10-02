import pygame
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys
from shot import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps = pygame.time.Clock()
    dt = .03
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable
    Shot.containers = (updatable, drawable, shots)
    asteroid_field = AsteroidField()
    p1 = Player(SCREEN_WIDTH /2, SCREEN_HEIGHT /2)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for i in updatable:
            i.update(dt)
            if i == p1:
                i.cooldown -= dt
        for i in asteroids:
            if p1.collide(i):
                print("Game over")
                sys.exit()
            
            for b in shots:
                if b.collide(i):
                    b.kill()
                    i.kill()

        screen.fill("black")
        for i in drawable:
            i.draw(screen)
        pygame.display.flip()
        fps.tick(60)













if __name__ == "__main__":
    main()