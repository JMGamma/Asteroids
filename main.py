import sys, pygame, constants
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    pygame.init
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    ship = Player((constants.SCREEN_WIDTH / 2), (constants.SCREEN_HEIGHT / 2))
    field = AsteroidField()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.Surface.fill(screen, ("black"))
        updatable.update(dt)
        for item in drawable:
            item.draw(screen)
        for asteroid in asteroids:
            if ship.collision_check(asteroid) == True:
                print("Game over!")
                sys.exit()
        pygame.display.flip()

        dt = clock.tick(60) /1000
        
    

if __name__ == "__main__":
    main()
