import pygame, circleshape, constants, random

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    

    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, width = 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20,50)
            vec1 = self.velocity.rotate(angle)
            vec2 = self.velocity.rotate(-angle)
            new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
            new1 = Asteroid(self.position.x, self.position.y, new_radius)
            new2 = Asteroid(self.position.x, self.position.y, new_radius)
            new1.velocity = vec1 * 1.2
            new2.velocity = vec2 *1.2
