import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    time_clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    
    # amount of time has passed since the last frame
    dt = 0 

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
                

        passed_time = time_clock.tick(60)
        dt = passed_time / 1000

        screen.fill("black")

        for obj_updatable in updatable:
            obj_updatable.update(dt)

        for obj_drawable in drawable:
            obj_drawable.draw(screen)

        for asteroid in asteroids:
            if player.is_collid(asteroid):
                print("Game over!")
                return

        for asteroid in asteroids:
            for shot in shots:
                if shot.is_collid(asteroid):
                    shot.kill()
                    asteroid.split()

        pygame.display.flip()



if __name__ == "__main__":
    main()


#  ➜ asteroids (main) ✗ source venv/bin/activate