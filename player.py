import pygame, circleshape, constants

class Player(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, constants.PLAYER_RADIUS)
        self.rotation = 0
        self.pos_x = x
        self.pos_y = y
        self.player_shoot_cooldown = 0

        # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), width=2)

    def rotate(self, dt):
        self.rotation += (constants.PLAYER_TURN_SPEED * dt)

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt*-1)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(dt*-1)
        if keys[pygame.K_SPACE]:
            self.shoot(dt)
        self.player_shoot_cooldown -= dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * constants.PLAYER_SPEED * dt

    def shoot(self,dt):
        if self.player_shoot_cooldown <= 0:
            round = Shot(self.position.x, self.position.y, 5)
            round.velocity = pygame.Vector2(0,1).rotate(self.rotation)
            round.velocity *= constants.PLAYER_SHOT_SPEED
            self.player_shoot_cooldown = 0.3



class Shot(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = constants.SHOT_RADIUS
    
    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, width = 2)

    def update(self, dt):
        self.position += (self.velocity * dt)
    