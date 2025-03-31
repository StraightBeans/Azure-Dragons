from settings import *

class Collision_Sprite(pygame.sprite.Sprite):
    def __init__(self, position, size, groups):
        super().__init__(groups)
        self.image = pygame.Surface(size)
        self.image.fill("yellow") #purely to visualize collisions be sure to remove once tilemaps are ready
        self.rect = self.image.get_frect(center = position)

#Same as collision sprite, will be used to trigger battles instead of enabling collisions through the same overlap mechanic
class Battle_Sprite(pygame.sprite.Sprite):
    def __init__(self, position, size, groups, game, enemy_name):
        super().__init__(groups)
        self.image = pygame.Surface(size)
        self.image.fill("blue") #replace with enemies so that when they touch the battle begins also figure out how to remove the enemy when entering battle
        self.rect = self.image.get_frect(center = position)
        self.game = game
        self.enemy_name = enemy_name
    
    def start_battle(self): #Remove Battle_Sprite and enter_battle from main.py
        print(f"Entered Battle with {self.enemy_name}")
        self.game.enter_battle(self.enemy_name)
        self.kill()