from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        super().__init__(groups)
        self.image = pygame.image.load(join("sprites", "old_man", "idle", "idle0.png")).convert_alpha()
        self.rect = self.image.get_frect(center = position)
        self.direction = pygame.Vector2()
        self.velocity = 200

    def input(self):
        movekeys = pygame.key.get_pressed()
        self.direction.x = int(movekeys[pygame.K_RIGHT]) - int(movekeys[pygame.K_LEFT])
        self.direction.y = int(movekeys[pygame.K_DOWN]) - int(movekeys[pygame.K_UP])
        self.direction = self.direction.normalize() if self.direction else self.direction
    
    def move(self, delta_time):
        self.rect.center += self.direction * self.velocity * delta_time

    def update(self, delta_time):
        self.input()
        self.move(delta_time)