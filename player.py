from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, position, groups, collision_sprites, battle_sprites):
        super().__init__(groups)
        self.image = pygame.image.load(join("sprites", "old_man", "idle", "idle0.png")).convert_alpha()
        self.rect = self.image.get_frect(center = position)
        self.hitbox = self.rect.inflate(-60,0)
        self.direction = pygame.Vector2()
        self.velocity = 200
        self.collision_sprites = collision_sprites
        self.battle_sprites = battle_sprites
        #self.moveable = moveable #Toggle during battle

    def input(self):
        movekeys = pygame.key.get_pressed()
        self.direction.x = int(movekeys[pygame.K_RIGHT]) - int(movekeys[pygame.K_LEFT])
        self.direction.y = int(movekeys[pygame.K_DOWN]) - int(movekeys[pygame.K_UP])
        self.direction = self.direction.normalize() if self.direction else self.direction

        menukeys = pygame.key.get_just_pressed()
        #add keys to pause or quit

    def move(self, delta_time):
        self.hitbox.x += self.direction.x * self.velocity * delta_time
        self.collision("horizontal")
        self.hitbox.y += self.direction.y * self.velocity * delta_time
        self.collision("vertical")
        self.rect.center = self.hitbox.center

    def collision(self, direction): #Mimic collision by changing the player position when they overlap a collision sprite
        for sprite in self.collision_sprites:
            if sprite.rect.colliderect(self.hitbox):
                if direction == "horizontal":
                    if self.direction.x > 0:
                        self.hitbox.right = sprite.rect.left
                    elif self.direction.x < 0:
                        self.hitbox.left = sprite.rect.right
                else:
                    if self.direction.y < 0:
                        self.hitbox.top = sprite.rect.bottom
                    elif self.direction.y > 0:
                        self.hitbox.bottom = sprite.rect.top

    def enter_battle(self): #Remove overlapping battle sprite and enter into battle
        for sprite in self.battle_sprites:
            if sprite.rect.colliderect(self.hitbox):
                sprite.kill()
                print("Enter Battle")
                Battle(PLAYER_DATA[0], ENEMY_DATA[0])

    def update(self, delta_time):
        self.input()
        self.move(delta_time)
        self.enter_battle()