import sys

import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_event, log_state
from player import Player
from shot import Shot


def main():
    pygame.init()
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable
    Shot.containers = (updatable, drawable, shots)
    player: Player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
    asteroid_field: AsteroidField = AsteroidField()

    while True:
        log_state()
        game_clock = pygame.time.Clock()
        dt = game_clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)

        for d in drawable:
            d.draw(screen)
        for a in asteroids:
            for s in shots:
                if a.collides_with(s):
                    log_event("asteroid_shot")
                    a.split()
                    pygame.sprite.Sprite.kill(s)
            if a.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        pygame.display.flip()


#        print(dt)


if __name__ == "__main__":
    main()
