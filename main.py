import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from logger import log_event
import sys

def main():
  
    pygame.init()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.containers = (updatable, drawable, shots)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()
    clock = pygame.time.Clock()
    dt = 0
    player = Player(
    SCREEN_WIDTH / 2,
    SCREEN_HEIGHT / 2
)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    while True:
        dt = clock.tick(60) / 1000
       
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


        screen.fill((0, 0, 0))
        for drawables in drawable:
            drawables.draw(screen)
        for obj in updatable:
            obj.update(dt) 
        pygame.display.flip() 
        for asteroid in asteroids:
            if asteroid.collides_with(player):
             log_event("player_hit")
             print("Game over!")
             sys.exit()
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()

if __name__ == "__main__":
    main()
